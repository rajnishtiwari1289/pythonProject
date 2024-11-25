from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

class DriverRule(ABC):
    @abstractmethod
    def get_driver(self) -> WebDriver:
        """Abstract method to be implemented for returning a WebDriver instance."""
        pass
