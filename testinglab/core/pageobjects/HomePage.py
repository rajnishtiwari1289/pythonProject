from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from testinglab.core.pageobjects.CommonPageHelper import CommonPageHelper


class HomePage(CommonPageHelper):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

        # Define WebElements
        self.emailId = self.driver.find_element(By.XPATH, "//input[@id='email']")
        self.password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        self.submitBtn = self.driver.find_element(By.XPATH, "//button[@id='submit']")

    def enter_email_id(self, email: str):
        self.emailId.send_keys(email)

    def enter_password(self, pass_: str):
        self.password.send_keys(pass_)

    def login(self, email: str, pass_: str):
        self.enter_email_id(email)
        self.enter_password(pass_)
        self.submitBtn.click()
