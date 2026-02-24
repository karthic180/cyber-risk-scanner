Write-Host "Running tests with coverage..."
pytest --cov=core --cov-report=term-missing --cov-report=html

Write-Host "Opening coverage report..."
Start-Process htmlcov/index.html