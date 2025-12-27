# run_tests.ps1

# Stop immediately if any command fails
$ErrorActionPreference = "Stop"

# Activate the virtual environment
# Use the correct path for Windows PowerShell
& .\venv\Scripts\Activate.ps1

# Check if pytest is installed
if (-not (Get-Command pytest -ErrorAction SilentlyContinue)) {
    Write-Host "pytest is not installed in the virtual environment."
    exit 1
}

# Run the test suite
pytest

# Exit successfully
exit 0
