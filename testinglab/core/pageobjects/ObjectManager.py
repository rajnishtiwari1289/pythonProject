from testinglab.core.pageobjects.AddContactPage import AddContactPage
from testinglab.core.pageobjects.ContactDetailsPage import ContactDetailsPage
from testinglab.core.pageobjects.ContactListPage import ContactListPage
from testinglab.core.pageobjects.EditContactPage import EditContactPage
from testinglab.core.pageobjects.HomePage import HomePage


class ObjectManager:
    def __init__(self, driver):
        self.driver = driver
        self.homePage = None
        self.editContactPage = None
        self.contactListPage = None
        self.contactDetailsPage = None
        self.addContactPage = None

    def get_home_page(self):
        if self.homePage is None:
            self.homePage = HomePage(self.driver)
        return self.homePage

    def get_edit_contact_page(self):
        if self.editContactPage is None:
            self.editContactPage = EditContactPage(self.driver)
        return self.editContactPage

    def get_contact_list_page(self):
        if self.contactListPage is None:
            self.contactListPage = ContactListPage(self.driver)
        return self.contactListPage

    def get_contact_details_page(self):
        if self.contactDetailsPage is None:
            self.contactDetailsPage = ContactDetailsPage(self.driver)
        return self.contactDetailsPage

    def get_add_contact_page(self):
        if self.addContactPage is None:
            self.addContactPage = AddContactPage(self.driver)
        return self.addContactPage
