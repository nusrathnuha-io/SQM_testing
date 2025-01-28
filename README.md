# Swag Labs Login Automation Script

This project automates the testing of the login functionality on the [Swag Labs website](https://www.saucedemo.com/) using Selenium WebDriver. It includes tests for successful and invalid login scenarios.

## Features

- Automated testing of successful login with valid credentials
- Validation of error messages for invalid login attempts
- Chrome WebDriver integration
- Easy-to-follow setup instructions

## Prerequisites

Before running the scripts, ensure you have:

1. **Python 3.8+**
   - Download from [python.org](https://www.python.org/)
   - Check "Add Python to PATH" during installation

2. **Google Chrome Browser**
   - Download from [google.com/chrome](https://www.google.com/chrome/)

3. **ChromeDriver**
   - Download from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
   - Must match your Chrome browser version
   - Add to system PATH

## Project Structure

The project contains two main test scripts:

- `login_successful.py`: Tests successful login scenario
- `invalid_login.py`: Tests invalid login scenarios

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# For Windows:
.\env\Scripts\activate
# For macOS/Linux:
source env/bin/activate
```

### 2. Install Dependencies

```bash
pip install selenium webdriver-manager
```

## Running the Tests

Ensure your virtual environment is activated before running the tests.

```bash
# Run successful login test
python login_successful.py

# Run invalid login test
python invalid_login.py
```

## Test Scenarios

### Successful Login Test
- **Script**: `login_successful.py`
- **Credentials**:
  - Username: `standard_user`
  - Password: `secret_sauce`
- **Verification**: Checks for presence of `inventory_list` element after login

### Invalid Login Test
- **Script**: `invalid_login.py`
- **Credentials**:
  - Username: `wrong_user`
  - Password: `wrong_password`
- **Verification**: Checks for error message: "Epic sadface: Username and password do not match any user in this service"

## Troubleshooting

### Common Issues

1. **WebDriverException**
   - Verify ChromeDriver version matches your Chrome browser
   - Ensure ChromeDriver is in system PATH

2. **ModuleNotFoundError: No module named 'selenium'**
   - Check virtual environment is activated
   - Run: `pip install selenium webdriver-manager`

## Dependencies

- selenium
- webdriver-manager

## Acknowledgments

This project uses the Swag Labs demo website (https://www.saucedemo.com/) for educational purposes. Swag Labs is provided by Sauce Labs as a testing playground for automation practice.
