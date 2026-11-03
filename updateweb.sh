#!/usr/bin/env bash
# updateweb.sh: rebuild the HTML/PDF copies (when possible), then commit and push to GitHub.
#   ./updateweb.sh                 commit message = "Update <date>"
#   ./updateweb.sh "What changed"  your own message
#   ./updateweb.sh --no-build      skip the rebuild
# Works offline: if the markdown package cannot be installed or Chrome is missing, the rebuild is skipped
# or partial, and the push still happens.
set -u
cd "$(dirname "$0")"
BUILD=1; MSG=""
for a in "$@"; do case "$a" in --no-build) BUILD=0 ;; *) MSG="$a" ;; esac; done
MSG="${MSG:-Update $(date '+%Y-%m-%d %H:%M')}"

if [ "$BUILD" -eq 1 ]; then
  PY=python3
  if [ -x .venv/bin/python ]; then PY=.venv/bin/python; fi
  if ! "$PY" -c "import markdown" >/dev/null 2>&1; then
    echo "Installing the markdown package (needs internet; skipped if it fails)..."
    [ -x .venv/bin/python ] || python3 -m venv .venv >/dev/null 2>&1 || true
    if [ -x .venv/bin/python ]; then
      .venv/bin/pip install --quiet --timeout 15 --retries 1 markdown >/dev/null 2>&1 && PY=.venv/bin/python
    fi
  fi
  echo "Rebuilding pages and PDFs..."
  "$PY" tools/build.py --pdf || echo "Rebuild had problems; pushing what exists."
fi

git add -A
if git diff --cached --quiet; then echo "No changes to commit."; else git commit -q -m "$MSG" && echo "Committed: $MSG"; fi
git push origin "$(git rev-parse --abbrev-ref HEAD)" && echo "Pushed to $(git remote get-url origin)"
echo "Reminder: this repository is public unless you changed it. Settings > General > Change visibility."
