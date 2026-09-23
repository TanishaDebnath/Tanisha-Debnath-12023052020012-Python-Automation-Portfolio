import unittest

from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


class LoginUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        config = ConfigReader.get_config()

        cls.base_url = config["DEFAULT"]["base_url"]
        cls.email = config["LOGIN"]["email"]
        cls.password = config["LOGIN"]["password"]

        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login_page(self):

        self.driver.get(self.base_url)

        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)

        home_page.click_my_account()
        home_page.click_login()

        login_page.enter_email(self.email)
        login_page.enter_password(self.password)

        login_page.click_login()

        self.assertIn(
            "My Account",
            self.driver.title
        )

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()