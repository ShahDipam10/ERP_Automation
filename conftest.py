import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
    driver.maximize_window()
    yield driver
    driver.quit()
