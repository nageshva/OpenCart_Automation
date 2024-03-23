import time
import pytest
import selenium
from PageObjects.homepage import Home
from PageObjects.login_page import Login
from PageObjects.register_page import Register
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_registration:

    url = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_registarion_with_valid_data(self,setup):
        self.logger.info("****Verify registration with valid data*****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.rg=Register(self.driver)
        self.hp.navigate_to_register_page()
        self.rg.enter_registration_details("jacky", "janu", "ja78123@gmail.com", "9678798", '123456','123456')

        if self.driver.title=="Your Account Has Been Created!":
           self.logger.info("Test passed: Regisration success ")
           assert True
        else:
            self.logger.error("Test failed: Regisration unsuccess ")
            assert False

        self.driver.quit()

    def test_registarion_with_invalid_mobile(self, setup):
        self.logger.info("****Verify registration with invalid mobilenum*****")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.rg = Register(self.driver)
        self.hp.navigate_to_register_page()
        self.rg.enter_registration_details("jari","ja8pytestnu","c89123@gmail.com","1hk3456789",'12345','12345')


        if self.driver.title != "Your Account Has Been Created!":
            self.logger.info("Test passed:   ")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "registration.png")
            self.logger.error("Test failed: able to create account with invalid mobile number  ")
            assert False

        self.driver.quit()


    def test_registarion_with_Null_values(self, setup):
        self.logger.info("****Verify registration with null values*****")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp = Home(self.driver)
        self.rg = Register(self.driver)
        self.hp.navigate_to_register_page()
        self.rg.enter_registration_details("", "", "", "", '', '')

        assert self.rg.fname_error()=="First Name must be between 1 and 32 characters!"
