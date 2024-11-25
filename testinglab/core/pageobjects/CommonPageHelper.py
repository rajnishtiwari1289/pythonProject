from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonPageHelper:
    def __init__(self, driver):
        """
        Constructor to initialize WebDriver and locate elements.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Optional, if you need waits
        self.logout_btn = (By.ID, "logout")  # Locator for the logout button

    def logout(self):
        """
        Clicks the logout button.
        """
        logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_btn))
        logout_button.click()
