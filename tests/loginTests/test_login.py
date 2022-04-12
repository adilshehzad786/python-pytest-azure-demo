import pytest
from selenium import webdriver
from pathlib import *
from chromedriver_py import binary_path


class TestLogin(object):
    @pytest.fixture()
    def test_setup(self):
        try:
            global driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')

            self.driver = webdriver.Chrome(executable_path=binary_path, chrome_options=chrome_options)
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.close()
            self.driver.quit()
            print("Test Completed")
        except:
            print("Something is failing")

    def test_01_login(self, test_setup):
        try:
            self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
            self.driver.find_element_by_name("username").send_keys("admin")
            self.driver.find_element_by_name("password").send_keys("demo")
            self.driver.find_element_by_name("password").submit()
            x = self.driver.title
            assert x == "ParaBank | Accounts Overview"
        except:
            print("Something is failing")
            assert False
