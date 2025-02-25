import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_login import setup, login  # Import setup fixture

@pytest.mark.dependency()
def test_login(setup):
    """Call the reusable login function from test_login.py"""
    login(setup)


@pytest.mark.dependency(depends=["test_login"])
def test_verify_project_created(setup):
    """Verify that the newly created project appears in the project list"""
    driver = setup
    wait = WebDriverWait(driver, 10)

    try:
        project_locator = "//div[@class='item-left']//div[2]"

        project_element = wait.until(EC.presence_of_element_located((By.XPATH, project_locator)))

        if project_element.is_displayed():
            print("[PASS] Project is successfully created and visible in the list!")
        else:
            print("[FAIL] Project is not found!")
            pytest.fail("Project verification failed")

    except Exception as e:
        print("[FAIL] Error while verifying project creation:", e)
        pytest.fail("Project creation verification failed")
