#!/bin/bash

set -e

echo "🔍 Validating project..."

if [ ! -f "README.md" ]; then
    echo "❌ README.md not found!"
    exit 1
fi

echo "✅ README.md found."

echo "🎉 Validation successful!"