# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Check a pull request's title and body, which a squash merge writes to main as the commit message (AGENTS.md).

The file's first line is the title; the rest is the body.

Usage: check_pull_request.py <file>
"""
import pathlib
import re
import subprocess
import sys

TITLE = re.compile(r"^(feat|fix|perf|refactor|test|docs|build|ci|chore|revert)(\([a-z0-9-]+\))?!?: \S")
ISSUE = re.compile(r"\b(close[sd]?|fix(e[sd])?|resolve[sd]?|refs?) ([\w.-]+/[\w.-]+)?#\d+\b", re.IGNORECASE)
AGENT_KEYS = {"co-authored-by", "assisted-by", "agent-effort"}
AGENT_EMAILS = ("<noreply@anthropic.com>", "<noreply@openai.com>")
ASSISTED_BY = re.compile(r"^[a-z0-9-]+:[A-Za-z0-9._-]+( \S+)*$")
EFFORTS = {"minimal", "low", "medium", "high", "xhigh", "max"}


def main() -> int:
    text = pathlib.Path(sys.argv[1]).read_text()
    title, _, body = text.partition("\n")
    errors = []
    if not TITLE.match(title):
        errors.append("title: write it as 'type(scope): summary'")
    if not ISSUE.search(body):
        errors.append("body: link the issue with 'Closes #N', or 'Refs #N' when the issue stays open")

    parsed = subprocess.run(["git", "interpret-trailers", "--parse"], input=text,
                            capture_output=True, text=True, check=True).stdout
    trailers = [line.partition(": ") for line in parsed.splitlines()]
    written = [l for l in body.splitlines() if l.partition(":")[0].strip().lower() in AGENT_KEYS]
    if len(written) != len([k for k, _, _ in trailers if k.lower() in AGENT_KEYS]):
        errors.append("body: trailers go in the last paragraph, one per line, with no blank line between them")
    agents = [v for k, _, v in trailers if k.lower() == "co-authored-by" and v.endswith(AGENT_EMAILS)]
    assisted = [v for k, _, v in trailers if k.lower() == "assisted-by"]
    efforts = [v for k, _, v in trailers if k.lower() == "agent-effort"]
    if len(assisted) < len(agents):
        errors.append("body: each agent's Co-Authored-By needs an 'Assisted-by: <agent>:<model>' trailer")
    errors += [f"body: Assisted-by '{v}' should read '<agent>:<model>'" for v in assisted if not ASSISTED_BY.match(v)]
    errors += [f"body: Agent-Effort '{v}' is not one of {', '.join(sorted(EFFORTS))}" for v in efforts if v not in EFFORTS]

    for e in errors:
        print(f"error: {e}")
    print(f"pull request: {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
