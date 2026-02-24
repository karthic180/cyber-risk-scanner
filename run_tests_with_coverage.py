import subprocess
import sys

def run_tests():
    """Run tests with coverage"""
    try:
        # Ensure coverage tracks the core code by using --source argument
        subprocess.check_call([sys.executable, "-m", "coverage", "run", "--source=core", "-m", "pytest", "tests/"])
        
        # After the tests run, generate a coverage report
        subprocess.check_call([sys.executable, "-m", "coverage", "report", "-m"])  # Use the -m flag for missing lines
    except subprocess.CalledProcessError as e:
        print(f"Error while running tests: {e}")
        sys.exit(1)

def main():
    """Main function to execute test run"""
    print("Running tests with coverage...")
    run_tests()

if __name__ == "__main__":
    main()