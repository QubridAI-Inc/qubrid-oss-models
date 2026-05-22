#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if command -v python3 &>/dev/null; then
  PYTHON=python3
elif command -v python &>/dev/null; then
  PYTHON=python
else
  echo ""
  echo "  Python is not installed."
  echo "  Install Python 3.8+ and run: python3 app.py"
  echo ""
  exit 1
fi

echo ""
echo "  Starting Qwen3.7-Max Tester / Playground..."
echo "  Press Ctrl+C to stop the server."
echo ""

exec "$PYTHON" app.py
