import pytest
from selenium import webdriver
from ERP_Automation.utils.read_config import ReadConfig
from ERP_Automation.pages.login_page import LoginPage
from ERP_Automation.utils.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.dependency()
def test_login(setup):
    # """Test Case 1: User Login"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    baseURL = ReadConfig.get_config_value("common info", "baseURL")
    username = ReadConfig.get_config_value("common info", "username")
    password = ReadConfig.get_config_value("common info", "password")

    driver.get(baseURL)
    login_page = LoginPage(driver)
    login_page.login(username, password)

    try:
        no_button = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.POPUP_NO_BUTTON)))
        no_button.click()
        print("[PASS] Popup dismissed!")
    except Exception:
        print("[INFO] No popup found.")

    assert "projectlistview" in driver.current_url.lower()
    print("[PASS] Login successful!")

@pytest.mark.dependency(depends=["test_login"])
def test_click_new_project(setup):
    # """Test Case 2: Click on '+ New Project'"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        new_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.NEW_PROJECT_BUTTON)))
        new_project_button.click()
        print("[PASS] + New Project button clicked!")
    except Exception as e:
        print("[FAIL] Failed to click '+ New Project' button:", e)
        pytest.fail("New Project button not clickable")

@pytest.mark.dependency(depends=["test_click_new_project"])
def test_select_blank_project(setup):
#     """Test Case 3: Select 'Blank Project'"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        blank_project_option = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.BLANK_PROJECT_OPTION)))
        blank_project_option.click()
        print("[PASS] Blank Project option selected!")
    except Exception as e:
        print("[FAIL] Failed to select 'Blank Project' option:", e)
        pytest.fail("Blank Project option not clickable")

@pytest.mark.dependency(depends=["test_select_blank_project"])
def test_enter_project_details(setup):
#     """Test Case 4: Enter Project Details"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        project_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PROJECT_NAME_FIELD)))
        project_name_field.send_keys("DipamShah1")

        project_key_field = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PROJECT_KEY_FIELD)))
        project_key_field.send_keys("DDD")

        print("[PASS] Project details entered!")
    except Exception as e:
        print("[FAIL] Failed to enter project details:", e)
        pytest.fail("Project details entry failed")

@pytest.mark.dependency(depends=["test_enter_project_details"])
def test_select_category(setup):
#     """Test Case 5: Select Project Category -> In House"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CATEGORY_DROPDOWN)))
        category_dropdown.click()
        print("[PASS] Category dropdown clicked!")

        in_house_option = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.IN_HOUSE_OPTION)))
        in_house_option.click()
        print("[PASS] In House option selected!")
    except Exception as e:
        print("[FAIL] Failed to select Category -> In House:", e)
        pytest.fail("Category selection failed")

@pytest.mark.dependency(depends=["test_select_category"])
def test_click_next_buttons(setup):
#     """Test Case 6: Click Next Buttons Until 'Create Project'"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        while True:
            try:
                create_project_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Project')]")
                if create_project_button.is_displayed():
                    print("[PASS] Create Project button found! Stopping Next button clicks.")
                    break
            except:
                pass  # Ignore if not found

            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='cursor-pointer conditional-next-step btn border-radius-4-px white border-0 bg-blue']")
            ))
            next_button.click()
            print("[PASS] Next button clicked!")

    except Exception as e:
        print("[FAIL] Error while clicking Next button:", e)
        pytest.fail("Next button clicking failed")

@pytest.mark.dependency(depends=["test_click_next_buttons"])
def test_create_project(setup):
#     """Test Case 7: Click 'Create Project'"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        create_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='createprojectbtn_driver']")))
        create_project_button.click()
        print("\n[PASS] Create Project button clicked!")
    except Exception as e:
        print("[FAIL] Failed to click Create Project button:", e)
        pytest.fail("Create Project button not clickable")






    # Keeping browser open until manual exit
    input("Press Enter to close the browser...")
