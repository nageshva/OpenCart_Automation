from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:

# Driver Initialization
    def __init__(self, driver):
        self.driver = driver

    # Lets define the elements locators

    email_xpath="//input[@id='input-email']"
    password_xpath="//input[@id='input-password']"
    forgot_password_linktext="Forgotten Password"
    login_button_xpath="//input[@value='Login']"
    login_error_message_xpath="//div[@class='alert alert-danger alert-dismissible']"

#Write Actions methods for each Object/Web Elements

    def enter_your_email(self,email):
        self.driver.find_element(By.XPATH,self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_your_password(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_forgot_password(self):
        self.driver.find_element(By.LINK_TEXT,self.forgot_password_linktext).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def login_error_msg(self):
       return self.driver.find_element(By.XPATH,self.login_error_message_xpath).text

    def enter_login_details(self,email,password):
        self.enter_your_email(email)
        self.enter_your_password(password)
        self.click_on_login_button()











