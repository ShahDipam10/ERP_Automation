class Locators:
    # Login Page
    LOGIN_USERNAME = "//input[@id='username']"
    LOGIN_PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@id='loginBtn']"

    # Popup Notification
    POPUP_NO_BUTTON = "//button[contains(@class, 'outline-secondary')]"

    # New Project
    NEW_PROJECT_BUTTON = "//button[contains(text(), 'New Project')]"
    BLANK_PROJECT_OPTION = "//div[@id='createblankproject_driver']//button[@type='button']"

    # Project Details
    PROJECT_NAME_FIELD = "//div[@id='createprojectname_driver']//input[@id='inputId']"
    PROJECT_KEY_FIELD = "//div[@id='createprojectkey_driver']//input[@id='inputId']"

    # Category Selection
    CATEGORY_DROPDOWN = "//div[@id='createprojectcategory_driver']"
    IN_HOUSE_OPTION = "//div[@id='item2']"

