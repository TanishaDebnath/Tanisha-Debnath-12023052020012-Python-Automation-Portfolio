from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver():

        driver = webdriver.Chrome()

        driver.maximize_window()

        return driver