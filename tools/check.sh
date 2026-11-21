#!/bin/sh
# Runs every check CI runs. Needs uv (https://docs.astral.sh/uv/).
set -eu
cd "$(dirname "$0")/.."
status=0
uv run --quiet tools/check_public_text.py "$@" || status=1
# The checks are copies of the hub's; keep them the same.
hub=${PROJECT_FA_HUB:-../project-fa}
if [ -d "$hub/tools" ]; then
  for f in check_public_text.py check_pull_request.py; do
    cmp -s "tools/$f" "$hub/tools/$f" || { echo "error: tools/$f differs from the hub's copy" >&2; status=1; }
  done
else
  echo "note: no hub checkout at $hub, so the copied checks weren't compared with it" >&2
fi
exit $status
