# Swag Labs Login Automation Script

This project automates the testing of the login functionality on the [Swag Labs website](https://www.saucedemo.com/) using Selenium WebDriver. The script performs automated testing for:
- Successful Login
- Invalid Login

## Setup and Execution

### 1. Prerequisites

Make sure you have the following installed:

1. **Python 3.8+**
   - Download and install Python from [python.org](https://www.python.org/)
   - Ensure you check the box for "Add Python to PATH" during installation

2. **Google Chrome Browser**
   - Download and install Google Chrome from [google.com/chrome](https://www.google.com/chrome/)

3. **ChromeDriver**
   - Download the version that matches your Chrome browser from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
   - Add the ChromeDriver executable to your system's PATH

### 2. Clone or Download the Repository

```bash
git clone <repository-url>
```

Or download the repository as a ZIP file and extract it. Open the project folder in Visual Studio Code.

### 3. Environment Setup

#### Step 1: Create a Virtual Environment

1. Open a terminal in Visual Studio Code
2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
   - Windows:
   ```bash
   .\env\Scripts\activate
   ```
   - macOS/Linux:
   ```bash
   source env/bin/activate
   ```

#### Step 2: Install Required Dependencies
```bash
pip install selenium webdriver-manager
```

### 4. Running the Script

1. Ensure your virtual environment is active (you should see `(env)` in your terminal)
2. Run the script:
```bash
python test.py
```

## Project Structure

### Main Files
- `test.py`: Contains both successful and invalid login test scenarios

### Test Scenarios

1. **Successful Login**
   - Username: `standard_user`
   - Password: `secret_sauce`
   - Verification: Checks for `inventory_list` element on dashboard

2. **Invalid Login**
   - Username: `wrong_user`
   - Password: `wrong_password`
   - Verification: Checks for error message "Epic sadface: Username and password do not match any user in this service"

## Troubleshooting

### Common Issues

1. **WebDriverException**
   - Verify ChromeDriver version matches your Chrome browser
   - Check if ChromeDriver is in system PATH

2. **ModuleNotFoundError: No module named 'selenium'**
   - Ensure virtual environment is activated
   - Run: `pip install selenium webdriver-manager`

## Dependencies

Required Python packages:
- selenium
- webdriver-manager

Install using:
```bash
pip install selenium webdriver-manager
```

## Acknowledgments

This project uses the Swag Labs demo website for educational purposes. Swag Labs is a test website provided for practicing Selenium automation.
