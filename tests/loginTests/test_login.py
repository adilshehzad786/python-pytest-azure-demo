import pytest
from selenium import webdriver
from pathlib import *
from chromedriver_py import binary_path


class TestLogin():
      
    @pytest.fixture
    def test_setup(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')

            driver = webdriver.Chrome(executable_path=binary_path, chrome_options=chrome_options)
            driver.implicitly_wait(10)
            driver.maximize_window()
            driver.close()
            driver.quit()
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
