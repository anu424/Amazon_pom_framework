'''
@author : anushree
@email : anu@gmail.com
@date : 18/12/2019
'''

import time
from generic_utilities.webdriver_manager.generic_methods import GenericMethods
import utilities.custom_logger as cl
import logging

class HomePageSearchProduct(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # We are inheriting GenericMethods for webdriver(driver) using super() -->parameterized constructor
        super().__init__(driver)
        self.driver = driver
        self.search_Product_Name="twotabsearchtextbox"

    def SearchBox(self,productName):
        # using self keyword we can access the methods in generic_methods
        self.sendKeys(productName,self.search_Product_Name)

        time.sleep(3)


