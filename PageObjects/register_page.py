from selenium import webdriver
from selenium.webdriver.common.by import By

class Register:


# Lets define the elements locators
    firstname_id="input-firstname"
    lastname_id="input-lastname"
    email_xpath="//input[@id='input-email']"
    telephone_xpath="//input[@id='input-telephone']"
    password_xpath="//input[@id='input-password']"
    password_confirm_xpath="//input[@id='input-confirm']"
    Subscribe_Yes_xpath="//label[normalize-space()='Yes']"
    privacy_policy_xpath="//input[@name='agree']"
    continue_xpath="//input[@value='Continue']"
    firstname_error_xpath="//div[contains(text(),'First Name must be between 1 and 32 characters!')]"
    lastname_error_xpath="//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"
    email_error_xpath="//div[contains(text(),'E-Mail Address does not appear to be valid!')]"
    telephone_num_err_xpath="//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"
    password_err_xpath="//div[contains(text(),'Password must be between 4 and 20 characters!')]"


#Driver Initialization
    def __init__(self, driver):
        self.driver = driver

#Write Actions methods for each Object/Web Elements

    def enter_firstname(self,fname):
        self.driver.find_element(By.ID,self.firstname_id).clear()
        self.driver.find_element(By.ID, self.firstname_id).send_keys(fname)

    def enter_lastname(self,lname):
        self.driver.find_element(By.ID,self.lastname_id).clear()
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lname)

    def enter_email(self,mail):
        self.driver.find_element(By.XPATH,self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(mail)

    def enter_telephone(self,phonenum):
        self.driver.find_element(By.XPATH,self.telephone_xpath).clear()
        self.driver.find_element(By.XPATH,self.telephone_xpath).send_keys(phonenum)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enter_confirm_password(self,repeat_password):
        self.driver.find_element(By.XPATH,self.password_confirm_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_confirm_xpath).send_keys(repeat_password)

    def check_subscribe_yes(self):
        self.driver.find_element(By.XPATH,self.Subscribe_Yes_xpath).click()

    def check_privacy_policy(self):
        self.driver.find_element(By.XPATH,self.privacy_policy_xpath).click()

    def click_continue(self):
        self.driver.find_element(By.XPATH,self.continue_xpath).click()


    def fname_error(self):
       return self.driver.find_element(By.XPATH,self.firstname_error_xpath).text

    def enter_registration_details(self,fname,lname,email,telnum,pwrd,cpwrd):
        self.enter_firstname(fname)
        self.enter_lastname(lname)
        self.enter_email(email)
        self.enter_telephone(telnum)
        self.enter_password(pwrd)
        self.enter_confirm_password(cpwrd)
        self.check_subscribe_yes()
        self.check_privacy_policy()
        self.click_continue()












