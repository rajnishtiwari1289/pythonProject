from selenium.webdriver.common.by import By

from testinglab.core.pageobjects.CommonPageHelper import CommonPageHelper


class AddContactPage(CommonPageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = {
            "firstName": (By.ID, "firstName"),
            "lastName": (By.ID, "lastName"),
            "phone": (By.ID, "phone"),
            "street1": (By.ID, "street1"),
            "city": (By.ID, "city"),
            "submitbtn": (By.ID, "submit"),
            "cancelbtn": (By.ID, "cancel")
        }

    def add_contact(self, contact_data):
        if "fName" in contact_data and contact_data["fName"] is not None:
            self.driver.find_element(*self.locators["firstName"]).send_keys(contact_data["fName"])
        if "lName" in contact_data and contact_data["lName"] is not None:
            self.driver.find_element(*self.locators["lastName"]).send_keys(contact_data["lName"])
        if "phone" in contact_data and contact_data["phone"] is not None:
            self.driver.find_element(*self.locators["phone"]).send_keys(contact_data["phone"])
        if "street1" in contact_data and contact_data["street1"] is not None:
            self.driver.find_element(*self.locators["street1"]).send_keys(contact_data["street1"])
        if "city" in contact_data and contact_data["city"] is not None:
            self.driver.find_element(*self.locators["city"]).send_keys(contact_data["city"])

        self.driver.find_element(*self.locators["submitbtn"]).click()
