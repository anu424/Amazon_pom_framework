from generic_utilities.webdriver_manager.generic_methods import GenericMethods
from pages.home_page_search_product import HomePageSearchProduct as searchProd
import unittest
from generic_utilities.driver_manager.webdriver_factory import WebDriverFactory
# Searching the product in search box
class HomeSearchProduct(WebDriverFactory):


    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver

    def searchProduct(self,name):
        searchProd(self.driver).SearchBox(name)
        searchProd(self.driver).elementClick("//input[@value='Go']","xpath")




