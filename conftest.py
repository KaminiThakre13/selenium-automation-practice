import time
import pytest

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")
@pytest.fixture(scope='class', params=['edge'])
def _drivers(request):
    parameter = request.param
    if parameter == 'chrome':
        driver = webdriver.Chrome(options=opts)
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()

    driver.get('https://demowebshop.tricentis.com/')
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()

## _drivers --> driver
"""@pytest.fixture()
def _drivers():
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(20)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()"""
