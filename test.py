from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_successful(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(3)

    # Enter credentials and login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    try:
        driver.find_element(By.CLASS_NAME, "inventory_list")
        print(f"Login Successful for username: {username}")
    except:
        print("Unexpected error. Login may have failed.")

    driver.quit()


def invalid_login_test(username, password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(6)

    # Enter invalid credentials and attempt login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(6)

    try:
        # Look for an error message indicating invalid login
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error_message:
            print(f"Invalid login detected for username: {username} with error: {error_message.text}")
    except:
        print("Login error handling failed. Check the script or site structure.")

    driver.quit()


if __name__ == "__main__":
    print("Testing successful login...")
    login_successful("standard_user", "secret_sauce")
    
    print("Testing invalid login...")
    invalid_login_test("wrong_user", "wrong_password")

