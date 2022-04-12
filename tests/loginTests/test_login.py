import pytest
from selenium import webdriver
from pathlib import *
from chromedriver_py import binary_path
import sys

class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        try:
            global driver
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

    def test_title(self, test_setup):
        """
        Verify click and title of page
        :return: None
        """
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == self.driver.title

    

    def test_item(self, test_setup):
        """
        Verify item submission
        :return: None
        """
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)

        driver.find_element_by_id("addbutton").click()
        
        li6 = self.driver.find_element_by_name("li6")
        sys.stderr.write(li6)
        # assert sample_text in li6


