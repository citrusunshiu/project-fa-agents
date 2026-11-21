# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Fail if tracked files, commit messages in a range, or extra text files contain private identifiers (ADR-0010).

Generic patterns live here. Exact private terms never do: they come from a git-ignored
.public-text-denylist file and from the PUBLIC_TEXT_DENYLIST environment variable (one term per line).

Usage: check_public_text.py [--repo <path>] [--commits <range>] [--text <file> ...]
"""
import argparse
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATTERNS = {
    "local path": re.compile(r"/Users/[A-Za-z0-9._-]+|/home/[a-z][a-z0-9_-]*/|[A-Z]:\\Users\\"),
    "session link": re.compile(r"Claude-Session" r":|claude\.ai/code/session_"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
ALLOWED_EMAIL_SUFFIXES = ("@users.noreply.github.com", "@example.com", "@example.org")
ALLOWED_EMAILS = {"noreply@anthropic.com", "noreply@openai.com"}


def private_terms() -> list[str]:
    terms = os.environ.get("PUBLIC_TEXT_DENYLIST", "").splitlines()
    local = ROOT / ".public-text-denylist"
    if local.is_file():
        terms += local.read_text().splitlines()
    return [t.strip().lower() for t in terms if t.strip() and not t.startswith("#")]


def findings(text: str, terms: list[str]) -> list[str]:
    out = [label for label, rx in PATTERNS.items() if rx.search(text)]
    for email in EMAIL.findall(text):
        if email.lower() not in ALLOWED_EMAILS and not email.lower().endswith(ALLOWED_EMAIL_SUFFIXES):
            out.append("email address")
    lowered = text.lower()
    out += ["private term"] * any(t in lowered for t in terms)
    return out


def git(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=pathlib.Path, default=ROOT, help="check this repository instead of the one holding this script; private terms still load from this one")
    ap.add_argument("--commits", help="also check the messages of commits in this range, e.g. origin/main..HEAD")
    ap.add_argument("--text", action="append", default=[], help="also check this file, e.g. a pull request's title and body")
    a = ap.parse_args()
    terms = private_terms()
    repo = pathlib.Path(git(a.repo, "rev-parse", "--show-toplevel").strip())
    errors = []
    for name in git(repo, "ls-files", "-co", "--exclude-standard").split("\n"):
        path = repo / name
        if not name or not path.is_file() or name == ".public-text-denylist":
            continue
        try:
            lines = path.read_text().splitlines()
        except UnicodeDecodeError:
            continue  # binary
        for lineno, line in enumerate(lines, 1):
            for label in findings(line, terms):
                errors.append(f"{name}:{lineno}: {label}")
    if a.commits:
        for sha in git(repo, "rev-list", a.commits).split():
            meta = git(repo, "show", "-s", "--format=%an <%ae>%n%cn <%ce>%n%B", sha)
            for label in findings(meta, terms):
                errors.append(f"commit {sha[:12]}: {label}")
    for name in a.text:
        for lineno, line in enumerate(pathlib.Path(name).read_text().splitlines(), 1):
            for label in findings(line, terms):
                errors.append(f"{pathlib.Path(name).name}:{lineno}: {label}")
    for e in sorted(set(errors)):
        print(f"error: {e}")
    print(f"public text: {repo.name}: {len(terms)} private terms loaded; {len(set(errors))} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
