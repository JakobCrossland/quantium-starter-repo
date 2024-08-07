#!/bin/bash

VENV_PATH="venv/bin/activate"

if [ -f "$VENV_PATH" ]; then
    source "$VENV_PATH"
else
    echo "Virtual environment not found at $VENV_PATH"
    exit 1
fi

echo "Running test suite..."
pytest test_app.py

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed."
else
    echo "Some tests failed."
fi

exit $EXIT_CODE
