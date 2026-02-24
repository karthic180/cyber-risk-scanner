#!/bin/bash

echo "Running tests with coverage..."
pytest --cov=core --cov-report=term-missing --cov-report=html

echo "Opening coverage report..."
open htmlcov/index.html 2>/dev/null || xdg-open htmlcov/index.html