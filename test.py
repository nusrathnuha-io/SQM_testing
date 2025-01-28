from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

def log_action(message):
   
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def setup_driver():
   
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login_test(username, password, expected_success=True):
   
    driver = None
    try:
        driver = setup_driver()
        log_action(f"Starting login test for username: {username}")
        
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")
        
        # Wait for elements and perform login
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        if expected_success:
            # Check for successful login
            try:
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
                message = f"Login successful for username: {username}"
                print(message)
                log_action(message)
            except TimeoutException:
                message = f"Login failed unexpectedly for username: {username}"
                print(message)
                log_action(message)
                raise Exception(message)
        else:
            # Check for error message
            try:
                error_message = wait.until(EC.presence_of_element_located(
                    (By.XPATH, "//h3[@data-test='error']")))
                message = f"Invalid login detected for username: {username} with error: {error_message.text}"
                print(message)
                log_action(message)
            except TimeoutException:
                message = f"Error message not found for invalid login attempt with username: {username}"
                print(message)
                log_action(message)
                raise Exception(message)
                
    except Exception as e:
        error_message = f"Test failed with error: {str(e)}"
        print(error_message)
        log_action(error_message)
        
    finally:
        if driver:
            driver.quit()
            log_action("Browser session ended")

def main():
   
    print("Starting login tests...")
    log_action("Beginning test suite execution")
    
    # Test valid login
    login_test("standard_user", "secret_sauce", expected_success=True)
    
    # Test invalid login
    login_test("wrong_user", "wrong_password", expected_success=False)
    
    log_action("Test suite execution completed")
    print("All tests completed!")

if __name__ == "__main__":
    main()
