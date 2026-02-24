# Cyber Risk Scanner

[![Build Status](https://img.shields.io/github/workflow/status/karthic180/cyber-risk-scanner/CI)](https://github.com/karthic180/cyber-risk-scanner/actions)
[![Coverage Status](https://coveralls.io/repos/github/karthic180/cyber-risk-scanner/badge.svg?branch=master)](https://coveralls.io/github/karthic180/cyber-risk-scanner?branch=master)
[![License](https://img.shields.io/github/license/karthic180/cyber-risk-scanner)](https://github.com/karthic180/cyber-risk-scanner/blob/master/LICENSE)

## Description

The Cyber Risk Scanner is a tool designed to analyze and detect various cyber risks, including phishing attempts, SSL vulnerabilities, and domain risks.

## Features

- **SSL Checking**: Verifies the SSL certificate and checks if the domain is secure.
- **Whois Lookup**: Provides domain ownership information through Whois.
- **Port Scanning**: Analyzes open ports for potential vulnerabilities.
- **Risk Calculation**: Computes the overall risk based on domain attributes and security checks.

## Installation

To install and set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cyber-risk-scanner.git
   cd cyber-risk-scanner
````

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   * **Windows**: `.\venv\Scripts\activate`
   * **macOS/Linux**: `source venv/bin/activate`

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests and check the code coverage:

1. Ensure the virtual environment is activated.
2. Run the following command:

   ```bash
   python run_tests_with_coverage.py
   ```

## Running the Application

To run the web-based application:

1. Ensure the virtual environment is activated.
2. Run:

   ```bash
   python run.py
   ```

This will start the web application, accessible on `http://localhost:5000`.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```