import os
import subprocess
import sys
import venv

def create_virtualenv():
    """Create a virtual environment."""
    if not os.path.exists("./venv"):
        print("Creating virtual environment...")
        venv.create("./venv", with_pip=True)
    else:
        print("Virtual environment already exists.")

def install_requirements():
    """Install requirements from the requirements.txt."""
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def activate_virtualenv():
    """Activate the virtual environment."""
    activate_this = './venv/Scripts/activate_this.py'
    if os.path.exists(activate_this):
        exec(open(activate_this).read(), {'__file__': activate_this})
        print("Virtual environment activated.")
    else:
        print("Error: Unable to find activate_this.py.")

def run_tests():
    """Run tests."""
    print("Running tests with coverage...")
    subprocess.check_call([sys.executable, "-m", "coverage", "run", "-m", "pytest", "tests/"])

def report_coverage():
    """Generate a coverage report."""
    print("Generating coverage report...")
    subprocess.check_call([sys.executable, "-m", "coverage", "report"])
    subprocess.check_call([sys.executable, "-m", "coverage", "html"])

def main():
    create_virtualenv()
    install_requirements()
    activate_virtualenv()
    run_tests()
    report_coverage()

if __name__ == "__main__":
    main()