from selenium import webdriver

from testinglab.core.drivers.DriverRule import DriverRule


class ChromeDriver(DriverRule):
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()  # Equivalent to fullscreen
        driver.implicitly_wait(5)  # Set implicit wait timeout
        return driver

class EdgeDriver(DriverRule):
    def get_driver(self):
        driver = webdriver.Edge()
        driver.maximize_window()  # Maximize the Edge browser window
        return driver

class DriverType:
    _drivers = {
        "chrome": ChromeDriver(),
        "edge": EdgeDriver()
    }

    @staticmethod
    def get_driver(browser: str):
        browser = browser.lower()
        if browser in DriverType._drivers:
            return DriverType._drivers[browser].get_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser}")