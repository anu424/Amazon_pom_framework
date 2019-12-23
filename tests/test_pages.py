from pages.base_page import BasePage
from test_cases.home_scearch_product import HomeSearchProduct

import unittest
class Test_verifying(unittest.TestCase):
    def __init__(self,driver):
        self.driver = BasePage(driver)
    def test_verify_product_search(self):
        # self.driver.get(URL)
        # hs(self.driver).searchProduct("iphone")
        hp = HomeSearchProduct(self.driver)
        hp.searchProduct("iphone")


if __name__ == '__main__':
    unittest.main()
