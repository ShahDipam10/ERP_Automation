from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "email")  # Ensure this locator is correct
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        email_element = wait.until(EC.presence_of_element_located(self.username_input))
        email_element.send_keys(username)

        password_element = wait.until(EC.presence_of_element_located(self.password_input))
        password_element.send_keys(password)

        login_button_element = wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()
