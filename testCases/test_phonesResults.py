import time

import selenium
from PageObjects.homepage import Home
from PageObjects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_001_Login:

    url=ReadConfig.getApplicationURL()
    email=ReadConfig.getEmail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login_with_valid_credentials(self,setup):
        self.logger.info('** ** ** ** ** * Verifying item list ** **  ** **')
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp =Home(self.driver)
        self.hp.click_on_phonesPDAs()
        self.results=self.driver.find_elements(By.XPATH,"//div[@id='content']//div[2]//div[i]//div[@class='product-thumb']//img[1]")
        for i in range(len(self.results)) :
            img_element = self.driver.find_element(By.XPATH,
                                                   f"(//div[@id='content']//div[2]//div[{i + 1}]//div[@class='product-thumb']//img[1])")
            self.itemname = img_element.get_attribute('alt')
            print(self.itemname)