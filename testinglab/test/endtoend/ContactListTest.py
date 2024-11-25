import pytest
from testinglab.core.config.GlobalHelper import GlobalHelper
from testinglab.core.drivers.Driver import Driver
from testinglab.core.pageobjects.ObjectManager import ObjectManager


@pytest.fixture(scope="class")
def setup_class():
    # Set up class-wide configurations (like loading properties)
    GlobalHelper.load_property()

@pytest.fixture()
def setup_method():
    # Set up before each test method (driver initialization)
    driver = Driver().get_driver_object("chrome")
    yield driver
    driver.quit()  # Cleanup after the test

def test_add_contact_and_display(setup_class, setup_method):
    driver = setup_method

    object_manager = ObjectManager(driver)

    # Navigate to the home page
    driver.get(GlobalHelper.get_property("homePageURI"))

    # Log in to the application
    object_manager.get_home_page().login(GlobalHelper.get_property("username"), GlobalHelper.get_property("password"))

    # Click on 'Add New Contact' button
    object_manager.get_contact_list_page().click_on_add_new_contact_btn()

    # Prepare contact data
    contact_data = {
        "fName": "rajnish1",
        "lName": "tiwari1",
        "phone": "2123456789",
        "street1": "street1 address",
        "city": "indore"
    }

    # Add the contact
    object_manager.get_add_contact_page().add_contact(contact_data)

    # Display the contacts
    object_manager.get_contact_list_page().get_contacts()
