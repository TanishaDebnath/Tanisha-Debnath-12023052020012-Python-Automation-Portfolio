from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, "input.btn.btn-primary")

    warning_message = (By.CSS_SELECTOR, ".alert.alert-danger")

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_warning_message(self):
        return self.driver.find_element(*self.warning_message).text