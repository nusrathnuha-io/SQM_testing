# **Swag Labs Login Automation Script**

This project automates the testing of the login functionality on the **Swag Labs website** (https://www.saucedemo.com/). It uses **Selenium WebDriver** to perform tests for:

- **Successful Login**
- **Invalid Login**

---

## **Setup and Execution**

Follow these steps to set up the required environment and execute the script.

---

### **1. Prerequisites**

Make sure you have the following installed:

1. **Python 3.8+**  
   - Download and install Python from [python.org](https://www.python.org/).  
   - Ensure you check the box for **"Add Python to PATH"** during installation.

2. **Google Chrome Browser**  
   - Download and install Google Chrome if not already installed from [google.com/chrome](https://www.google.com/chrome/).

3. **ChromeDriver**  
   - Download the version of ChromeDriver that matches your Chrome browser version from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).  
   - Add the ChromeDriver executable to your system's PATH.

---

### **2. Project Files**

This project contains the following key files:

1. **`login_successful.py`**  
   - Handles automation of successful login functionality for Swag Labs.  
   - Tests for the following valid credentials:  
     - **Username**: `standard_user`  
     - **Password**: `secret_sauce`  
   - Verifies that the `inventory_list` element is displayed after login.

2. **`invalid_login.py`**  
   - Handles automation of invalid login scenarios.  
   - Tests for the following invalid credentials:  
     - **Username**: `wrong_user`  
     - **Password**: `wrong_password`  
   - Verifies the error message:  
     `"Epic sadface: Username and password do not match any user in this service."`

---

### **3. Environment Setup**

#### **Step 1: Create a Virtual Environment**

1. Open a terminal in **Visual Studio Code**.  
2. Create a virtual environment by running:
   ```bash
   python -m venv env
