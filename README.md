# QA-Automation-Portfolio

# 🧪 Software Quality Assurance (QA) Portfolio

Welcome to my **Software Quality Assurance Portfolio**, showcasing a complete range of QA skills — from **manual testing** to **test automation** and **low-code AI testing platforms**.

This repository demonstrates my ability to design, automate, and execute tests in different environments and methodologies.

---

## 🧩 What’s Inside

1. 📝 **Manual Test Case Design**  
2. 🤖 **Coded Test Automation (Python + Selenium)**  
3. ⚡ **Low-Code Platform Automation (TestRigor)**  

All examples are based on the **OrangeHRM** demo application — a real-world, open-source HR management system.

---

## 🌐 1. System Under Test (SUT)

**Application:** [OrangeHRM (Open Source HR Management System)](https://opensource-demo.orangehrmlive.com/)  
**Type:** Web-based HR portal  
**Purpose:** Manage users, employees, and personal information  

---

## 🧾 2. Foundational Skill: Manual Test Case Design

📁 **Folder:** [`/manual-test-cases/`](./manual-test-cases/)

This section demonstrates my ability to **analyze an application** and create a **comprehensive manual test suite**.

**✅ Includes:**
- Test Scenarios and Test Cases  
- Detailed Test Steps and Expected Results  
- Execution logs (Pass/Fail tracking)  

**🎯 Modules Covered:**
- Login  
- Add User  
- Logout  
- Personal Details  

**🧠 What it shows:**
- Analytical thinking for test design  
- Understanding of functional flows  
- Documentation clarity and precision  

---

## 💻 3. Core Skill: Test Automation (Python + Selenium)

📁 **Folder:** [`/selenium-python-scripts/`](./selenium-python-scripts/)

This section contains **Python-based automation scripts** built using the **Selenium WebDriver** library.

These scripts convert the manual test cases into a **repeatable, reliable automation suite**.

**🔧 Tech Stack:**
- `Python 3`
- `Selenium WebDriver`
- `unittest` or `pytest` framework (optional)
- ChromeDriver  

**💡 Skills Demonstrated:**
- Writing and executing Selenium tests  
- Locating elements via CSS, Name, and XPath  
- Performing actions (`click`, `send_keys`, etc.)  
- Using assertions to validate expected results  

---

### 🧰 Example Script: `test_orangehrm_login.py`

```python
# 🧪 Automated Test: OrangeHRM Valid Login
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

try:
    # Step 1: Enter username
    driver.find_element(By.NAME, "username").send_keys("Admin")

    # Step 2: Enter password
    driver.find_element(By.NAME, "password").send_keys("admin123")

    # Step 3: Click 'Login'
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    # Step 4: Verify successful login
    heading = driver.find_element(By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module").text
    if "Dashboard" in heading:
        print("✅ TEST PASSED: Login Successful!")
    else:
        print("❌ TEST FAILED: Dashboard not found.")
except Exception as e:
    print(f"❌ TEST FAILED: Error occurred - {e}")
finally:
    driver.quit()
