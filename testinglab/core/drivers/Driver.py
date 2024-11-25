from testinglab.core.drivers.DriverType import DriverType


class Driver:
    def get_driver_object(self, browser):
        return DriverType.get_driver(browser)
