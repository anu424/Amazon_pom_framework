from test_cases.home_scearch_product import HomeSearchProduct
from generic_utilities.driver_manager.webdriver_factory import WebDriverFactory as wd
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class Test_AmazonProj():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.a = wd(self.driver)
        self.hs = HomeSearchProduct(self.driver)

    # @pytest.mark.run(order=1)
    def test_searchProduct(self):
        self.hs.searchProduct("iphone")

"""
OUTPUT:
py.test  -v -s test_runner.py --browser firefox
py.test  -v -s test_runner.py --browser chrome


TO GENERATE HTML REPORT :
PREREQUISITE: 
        pip install pytest-HTML



TO GENERATE A REPORT : 
py.test -x test_runner.py --browser chrome --html=Amazon_searchProduct.html

"""
