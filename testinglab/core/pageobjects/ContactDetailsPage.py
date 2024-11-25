from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactDetailsPage:
    def __init__(self, driver):
        """
        Constructor to initialize WebDriver and element locators.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # WebDriverWait for dynamic elements
        self.locators = {
            "editContactBtn": (By.ID, "edit-contact"),
            "returnToListBtn": (By.ID, "return"),
            "deleteBtn": (By.ID, "delete")
        }

    def click_on_edit_contact_btn(self):
        """
        Clicks the 'Edit Contact' button.
        """
        edit_button = self.wait.until(EC.element_to_be_clickable(self.locators["editContactBtn"]))
        edit_button.click()

    def click_on_return_btn(self):
        """
        Clicks the 'Return to List' button.
        """
        return_button = self.wait.until(EC.element_to_be_clickable(self.locators["returnToListBtn"]))
        return_button.click()

    def click_on_delete_btn(self):
        """
        Clicks the 'Delete' button and accepts the confirmation alert.
        """
        delete_button = self.wait.until(EC.element_to_be_clickable(self.locators["deleteBtn"]))
        delete_button.click()
        alert = self.wait.until(EC.alert_is_present())  # Wait for the alert to appear
        alert.accept()  # Accept the confirmation alert
