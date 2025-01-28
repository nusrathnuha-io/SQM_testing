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
git clone https://github.com/nusrathnuha-io/SQM_testing

```

Or download the repository as a ZIP file and extract it. Open the project folder in Visual Studio Code.

### 3. Environment Setup



1. Create a conda environment:
```bash
conda create --name SQM_env python=3.9 -y

```

2. Activate the conda environment:
```bash
conda activate SQM_env
```

### 4. Install Required Dependencies

After activating either environment, install the required packages:
```bash
pip install selenium webdriver-manager
```

### 5. Running the Script

1. Ensure your environment is active:
   - For venv: You should see `(env)` in your terminal
   - For conda: You should see `(SQM_env)` in your terminal
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

![web page openning](https://github.com/user-attachments/assets/2aea91f8-67c2-4e6a-b896-a774ba8e870a)


![Succesful login](https://github.com/user-attachments/assets/be7bc5af-7860-41f9-9571-6190d1524dae)

![login successfull message  in terminal](https://github.com/user-attachments/assets/44119434-dc9f-4563-b781-9447f6c5566e)




2. **Invalid Login**
   - Username: `wrong_user`
   - Password: `wrong_password`
   - Verification: Checks for error message "Epic sadface: Username and password do not match any user in this service"

![Invalid login](https://github.com/user-attachments/assets/4c82057f-c8cf-449d-ba76-f753a953e3d8)
![invalid login message in terminal](https://github.com/user-attachments/assets/5d73437d-d698-4872-96d5-308b793763b3)

## Troubleshooting

### Common Issues

1. **WebDriverException**
   - Verify ChromeDriver version matches your Chrome browser
   - Check if ChromeDriver is in system PATH

2. **ModuleNotFoundError: No module named 'selenium'**
   - Ensure your chosen environment (venv or conda) is activated
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
