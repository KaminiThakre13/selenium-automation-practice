class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, logical_name):
        self.driver.find_element(*logical_name).click()

    def enter_data(self, logical_name, data):
        self.driver.find_element(*logical_name).send_keys(data)