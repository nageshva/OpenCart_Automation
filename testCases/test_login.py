import time

import pytest
import selenium
from PageObjects.homepage import Home
from PageObjects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    url=ReadConfig.getApplicationURL()
    # email=ReadConfig.getEmail()
    # password=ReadConfig.getPassword()
    logger = LogGen.loggen()
    @pytest.mark.parametrize( "email,password",
        [
            ("haribash@gmail.com","Abc@123"),
            ("smaccmt@gmail.com","123456")
        ]

    )
    def test_login_with_valid_credentials(self,setup,email,password):
        self.logger.info('** ** ** ** ** * Verifying Login test ** **  ** **')
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp =Home(self.driver)
        self.lp=Login(self.driver)
        self.hp.navigate_to_login_page()
        self.lp.enter_login_details(email,password)

        if self.driver.title == "My Account":
            self.logger.info("Test Passed: User successfully logged in and landed on the My Account page")
            assert True
        else:
            self.logger.error("Test Failed: User was unable to log in or was not redirected to the My Account page")
            assert False

        self.driver.quit()

    # def test_login_with_invalid_email(self,setup):
    #     self.logger.info("*****Verifying Login with invalid email********")
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.hp = Home(self.driver)
    #     self.lp = Login(self.driver)
    #     self.hp.navigate_to_login_page()
    #     self.lp.enter_login_details("haribash.com", "Abc@123")
    #
    #     if self.lp.login_error_msg()=="Warning: No mtch for E-Mail Address and/or Password.":
    #         self.logger.info("Test Passed: User unable to logged in and was not landed on the My Account page")
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
    #         self.logger.error("Test Failed: User was able to log in or redirected to the My Account page")
    #         assert False
    #
    #     self.driver.quit()






