from selenium.webdriver.common.by import By
from testinglab.core.pageobjects.CommonPageHelper import CommonPageHelper

class EditContactPage(CommonPageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Define WebElements
        self.firstName = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
        self.lastName = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
        self.phone = self.driver.find_element(By.XPATH, "//input[@id='phone']")
        self.street1 = self.driver.find_element(By.XPATH, "//input[@id='street1']")
        self.city = self.driver.find_element(By.XPATH, "//input[@id='city']")
        self.submitbtn = self.driver.find_element(By.XPATH, "//button[@id='submit']")
        self.cancelbtn = self.driver.find_element(By.XPATH, "//button[@id='cancel']")

    def enter_first_name(self, first_name: str):
        self.firstName.send_keys(first_name)
        return self

    def enter_last_name(self, last_name: str):
        self.lastName.send_keys(last_name)
        return self

    def enter_phone(self, phone: str):
        self.phone.send_keys(phone)
        return self

    def enter_street1(self, street1: str):
        self.street1.send_keys(street1)
        return self

    def enter_city(self, city: str):
        self.city.send_keys(city)
        return self

    def click_submit(self):
        self.submitbtn.click()
        return self

    def click_cancel(self):
        self.cancelbtn.click()
        return self
