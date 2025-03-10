import time

'''class Register:

    def __init__(self,driver):
        self.driver = driver
    def click_on_register(self):

        self.driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def select_gender(self):
        self.driver.find_element('xpath', '//input[@id="gender-female"]').click()

    def enter_firstname(self):

        self.driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Harry')

    def enter_lastname(self):
        self.driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Potter')

    def enter_email(self):

        self.driver.find_element('xpath', '//input[@id="Email"]').send_keys('hpotter@gmail.com')

    def set_password(self):

        self.driver.find_element('xpath', '//input[@id="Password"]').send_keys('Harryis@')

    def confirm_password(self):

        self.driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('Harryis@')

'''
from data_.reading_excel import reg_data
from library_.wrapperfunction import SeleniumWrapper

locators = reg_data()

class Register:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver=webdriver.Chrome()
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def click_on_register(self):
        self.sel_wrap_obj.click_on_element(locators['register'])
        time.sleep(5)

    def select_gender(self):
        self.sel_wrap_obj.click_on_element(locators['gender'])

    def enter_firstname(self):
        self.sel_wrap_obj.enter_data(locators['firstname'], 'Sherlock')

    def enter_lastname(self):
        self.sel_wrap_obj.enter_data(locators['lastname'], 'Holmes')

    def enter_email(self):
        self.sel_wrap_obj.enter_data(locators['email'], 'sherlock@gmail.com')

    def set_password(self):
        self.sel_wrap_obj.enter_data(locators['password'], 'sherlock@12345')

    def confirm_password(self):
        self.sel_wrap_obj.enter_data(locators['confirm_password'], 'sherlock@12345')
