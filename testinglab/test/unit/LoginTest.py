import pytest

from testinglab.core.config.GlobalHelper import GlobalHelper
from testinglab.core.drivers.Driver import Driver
from testinglab.core.pageobjects.HomePage import HomePage


@pytest.fixture(scope="class")
def setup_class():
    # Set up class-wide configurations (like loading properties)
    GlobalHelper.load_property()

@pytest.fixture()
def setup_method():
    # Set up before each test method (driver initialization)
    driver = Driver().get_driver_object("chrome")
    # pass driver to test method
    yield driver
    #below code execute after test finished
    driver.quit()  # Cleanup after the test

def test_login(setup_class, setup_method):
    driver = setup_method
    # Navigate to the home page
    driver.get(GlobalHelper.get_property("homePageURI"))
    home_page = HomePage(driver)

    # Perform login action
    home_page.login(GlobalHelper.get_property("username"), GlobalHelper.get_property("password"))
