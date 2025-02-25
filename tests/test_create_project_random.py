import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ERP_Automation.utils.locators import Locators
from .test_login import login  # Use relative import (dot before test_login)


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.dependency()
def test_login(setup):
    """Call the reusable login function from test_login.py"""
    login(setup)


@pytest.mark.dependency(depends=["test_login"])
def test_create_project_random(setup):
    """Create a new project with a random name"""
    driver = setup
    wait = WebDriverWait(driver, 10)



    # Click on '+ New Project'
    new_project_button = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.NEW_PROJECT_BUTTON)))
    new_project_button.click()
    print("[PASS] Clicked '+ New Project' button!")

    # Select 'Blank Project'
    blank_project_option = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.BLANK_PROJECT_OPTION)))
    blank_project_option.click()
    print("[PASS] Selected 'Blank Project' option!")

    # Generate Random Project Name and Key
    random_project_name = "Project_" + str(uuid.uuid4())[:8]  # Shortened UUID
    random_project_key = str(uuid.uuid4())[:3].upper()  # Shortened key

    # Enter Project Name
    project_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PROJECT_NAME_FIELD)))
    project_name_field.send_keys(random_project_name)

    # Enter Project Key
    project_key_field = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.PROJECT_KEY_FIELD)))
    project_key_field.send_keys(random_project_key)

    print(f"[PASS] Entered Project Name: {random_project_name}")
    print(f"[PASS] Entered Project Key: {random_project_key}")

    # Select Project Category
    category_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.CATEGORY_DROPDOWN)))
    category_dropdown.click()
    in_house_option = wait.until(EC.element_to_be_clickable((By.XPATH, Locators.IN_HOUSE_OPTION)))
    in_house_option.click()
    print("[PASS] Selected 'In House' category!")

    # Click 'Next' until 'Create Project' button appears
    while True:
        try:
            create_project_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Project')]")
            if create_project_button.is_displayed():
                print("[PASS] 'Create Project' button found! Stopping 'Next' clicks.")
                break
        except:
            pass  # Ignore if not found

        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='cursor-pointer conditional-next-step btn border-radius-4-px white border-0 bg-blue']")))
        next_button.click()
        print("[PASS] Clicked 'Next' button!")

    # Click 'Create Project'
    create_project_button.click()
    print("\n[PASS] Clicked 'Create Project' button!")

