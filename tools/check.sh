#!/bin/sh
# Runs every check CI runs. Needs uv (https://docs.astral.sh/uv/).
set -eu
cd "$(dirname "$0")/.."
status=0
uv run --quiet tools/check_public_text.py "$@" || status=1
# The checks are copies of the hub's; keep them the same. The hub's main checkout sits beside this
# repository's main checkout, which a linked worktree finds through git's common directory.
main_checkout=$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")
hub=${PROJECT_FA_HUB:-$main_checkout/../project-fa}
if [ -d "$hub/tools" ]; then
  for f in check_public_text.py check_pull_request.py; do
    cmp -s "tools/$f" "$hub/tools/$f" || { echo "error: tools/$f differs from the hub's copy" >&2; status=1; }
  done
elif [ -n "${CI:-}" ]; then
  echo "note: CI has no hub checkout, so the copied checks weren't compared with it" >&2
else
  echo "error: no hub checkout at $hub; clone the hub beside this repository or set PROJECT_FA_HUB" >&2
  status=1
fi
exit $status
