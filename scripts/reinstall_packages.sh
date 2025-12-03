#!/bin/bash

# Script to uninstall and reinstall the package
# This helps refresh dependencies and resolve installation issues

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=================================="
echo "Uninstalling job-scrapper-contracts..."
echo "=================================="

# Uninstall the package
pip uninstall -y job-scrapper-contracts 2>/dev/null || echo "  (not installed, skipping)"

echo ""
echo "=================================="
echo "Reinstalling job-scrapper-contracts..."
echo "=================================="

# Reinstall the package in editable mode with dev dependencies
cd "$PROJECT_ROOT"
pip install -e ".[dev]"

echo ""
echo "=================================="
echo "Done! Package reinstalled."
echo "=================================="
