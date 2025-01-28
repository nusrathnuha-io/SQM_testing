Swag Labs Login Automation Script
This project automates the testing of the login functionality on the Swag Labs website (https://www.saucedemo.com/). It uses Selenium WebDriver to perform tests for:

Successful Login
Invalid Login
Setup and Execution
Follow these steps to set up the required environment and execute the script.

1. Prerequisites
Make sure you have the following installed:

Python 3.8+
Download and install Python from python.org.
Google Chrome Browser
Download and install Google Chrome if not already installed.
ChromeDriver
Download the version of ChromeDriver that matches your Chrome browser version from chromedriver.chromium.org.
Add the ChromeDriver executable to your system's PATH.
2. Clone or Download the Repository
Clone this repository using the following command:

bash
Copy
Edit
git clone <repository-url>
Or download the repository as a ZIP and extract it.

Open the project folder in Visual Studio Code.

Environment Setup
Step 1: Create a Virtual Environment
Open a terminal in Visual Studio Code.
Create a virtual environment by running:
bash
Copy
Edit
python -m venv env
Activate the virtual environment:
On Windows:
bash
Copy
Edit
.\env\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source env/bin/activate
Step 2: Install Required Dependencies
Run the following command to install Selenium and WebDriver Manager:

bash
Copy
Edit
pip install selenium webdriver-manager
How to Run the Script
Open Visual Studio Code and ensure the virtual environment is active (you should see (env) at the start of your terminal prompt).
Run the script using the following command:
bash
Copy
Edit
python test.py
How It Works
Files in the Project
test.py
The main script file that tests the login functionality for both valid and invalid login scenarios.
Test Scenarios
Successful Login:
Username: standard_user
Password: secret_sauce
The test verifies that the inventory_list element is present on the dashboard after login.
Invalid Login:
Username: wrong_user
Password: wrong_password
The test verifies the error message: "Epic sadface: Username and password do not match any user in this service."
Troubleshooting
WebDriverException:
Make sure ChromeDriver is installed and matches your Chrome browser version.

Error: ModuleNotFoundError: No module named 'selenium':
Ensure you’ve activated the virtual environment and installed the required libraries using pip install selenium webdriver-manager.

Dependencies
The following Python packages are required:

selenium
webdriver-manager
Install them using:

bash
Copy
Edit
pip install selenium webdriver-manager
Acknowledgments
This project uses the Swag Labs demo website for educational purposes. Swag Labs is a test website for practicing Selenium automation.

