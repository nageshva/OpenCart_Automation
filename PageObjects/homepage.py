
from selenium import webdriver
from selenium.webdriver.common.by import By

class Home:
    # Lets define the elements locators


    myaccount_xpath = "//span[normalize-space()='My Account']"
    Register_linktext = "Register"
    Login_linktext = "Login"
    Phones_PDAs_xpath="//a[normalize-space()='Phones & PDAs']"



#Driver Initialization
    def __init__(self, driver):
        self.driver = driver


#Write Actions methods for each Object/Web Elements

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH,self.myaccount_xpath).click()

    def click_on_Register(self):
        self.driver.find_element(By.LINK_TEXT,self.Register_linktext).click()

    def click_on_login(self):
        self.driver.find_element(By.LINK_TEXT,self.Login_linktext).click()


    def click_on_phonesPDAs(self):
        self.driver.find_element(By.XPATH,self.Phones_PDAs_xpath).click()

    def navigate_to_login_page(self):
        self.click_on_my_account()
        self.click_on_login()

    def navigate_to_register_page(self):
        self.click_on_my_account()
        self.click_on_Register()









