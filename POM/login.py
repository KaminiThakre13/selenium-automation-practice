import time
'''
class Login:

    def __init__(self,driver):
        self.driver = driver
    def click_on_login(self):

        self.driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(1)

    def enter_login_email(self):

        self.driver.find_element('xpath', '//input[@id="Email"]').send_keys('hpotter@gmail.com')

    def click_on_password(self):

        self.driver.find_element('xpath', '//input[@id="Password"]').send_keys('Harryis@')

'''
from data_.reading_excel import login_data
from library_.wrapperfunction import SeleniumWrapper

locators = login_data()

class Login:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver = webdriver.Chrome()
        self.sel_wrap_obj = SeleniumWrapper(self.driver)

    def click_on_login(self):
        self.sel_wrap_obj.click_on_element(locators['login'])
        time.sleep(1)

    def enter_login_email(self):
        self.sel_wrap_obj.enter_data(locators['email'], 'sherlock@gmail.com')

    def click_on_password(self):
        self.sel_wrap_obj.enter_data(locators['password'], 'sherlock@12345')