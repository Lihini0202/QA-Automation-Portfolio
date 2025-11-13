# test_orangehrm_login.py
# This script automates the "Valid Login" test case for OrangeHRM.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the OrangeHRM demo site
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2) # Wait for page to load

try:
    # 1. Enter valid username
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("Admin")

    # 2. Enter valid password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")

    # 3. Click 'Login'
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    time.sleep(3) # Wait for dashboard to load

    # 4. Verify login by checking for "Dashboard" heading
    heading = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module").text
    
    if "Dashboard" in heading:
        print("✅ TEST PASSED: Login Successful. Dashboard is visible.")
    else:
        print("❌ TEST FAILED: Login Failed. Dashboard not found.")

except Exception as e:
    print(f"❌ TEST FAILED: An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
