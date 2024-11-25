from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactListPage:
    def __init__(self, driver):
        """
        Constructor to initialize WebDriver and element locators.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # WebDriverWait for dynamic elements
        self.locators = {
            "addNewContactBtn": (By.ID, "add-contact")
        }

    def click_on_contact(self, contact_name):
        """
        Clicks on the contact row matching the given contact name.
        """
        contact_xpath = f"//td[contains(text(),'{contact_name.upper()}')]"
        try:
            contact_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, contact_xpath)))
            contact_element.click()
        except Exception as e:
            print(f"Error: Contact '{contact_name}' not found. {e}")

    def click_on_add_new_contact_btn(self):
        """
        Clicks the 'Add New Contact' button.
        """
        add_contact_button = self.wait.until(EC.element_to_be_clickable(self.locators["addNewContactBtn"]))
        add_contact_button.click()

    def get_contacts(self):
        """
        Prints all contact details from the contact list table.
        """
        row_xpath = "//tr"
        rows = self.driver.find_elements(By.XPATH, row_xpath)

        for i, row in enumerate(rows, start=1):
            cells_xpath = f"//tr[{i}]/td"
            cells = self.driver.find_elements(By.XPATH, cells_xpath)
            row_text = " | ".join(cell.text for cell in cells)
            print(row_text)
