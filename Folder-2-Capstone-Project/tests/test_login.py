from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader


# Read configuration
config = ConfigReader.get_config()


def test_valid_login(driver):

    driver.get(config["DEFAULT"]["base_url"])

    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.click_my_account()
    home_page.click_login()

    # Get credentials from config.ini
    login_email = config["LOGIN"]["email"]
    login_password = config["LOGIN"]["password"]

    login_page.enter_email(login_email)
    login_page.enter_password(login_password)

    login_page.click_login()

    assert "My Account" in driver.title


def test_invalid_login(driver):

    driver.get(config["DEFAULT"]["base_url"])

    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.click_my_account()
    home_page.click_login()

    # Deliberately invalid credentials
    login_page.enter_email("wrong@example.com")
    login_page.enter_password("wrongpassword")

    login_page.click_login()

    message = login_page.get_warning_message()

    assert "Warning" in message