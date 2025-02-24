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

def login(driver):
    """Reusable Login Function"""
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
        print("[PASS] Welcome u r in.")
    except Exception:
        print("[INFO] sry")

    assert "projectlistview" in driver.current_url.lower()
    print("[PASS] Login successful!")
