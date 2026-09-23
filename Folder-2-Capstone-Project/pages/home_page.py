from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account = (By.XPATH, "//span[text()='My Account']")
    login_link = (By.LINK_TEXT, "Login")

    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def click_my_account(self):
        self.driver.find_element(*self.my_account).click()

    def click_login(self):
        self.driver.find_element(*self.login_link).click()

    def search_product(self, product):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(product)
        self.driver.find_element(*self.search_button).click()