from selenium import webdriver
from constants.constant_variable import *
from generic_utilities.webdriver_manager.generic_methods import GenericMethods
class WebDriverFactory(GenericMethods):
    def __init__(self, driver):
        super(WebDriverFactory, self).__init__(driver)
        self.driver = driver

    def getWebDriverInstance(self):
        if self.driver == 'firefox':
            driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)
        return driver
