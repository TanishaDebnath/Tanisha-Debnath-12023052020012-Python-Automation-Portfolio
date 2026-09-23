from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    search_heading = (By.XPATH, "//h1[contains(text(), 'Search')]")
    search_results = (By.CSS_SELECTOR, ".product-thumb")

    def get_search_heading(self):
        return self.driver.find_element(*self.search_heading).text

    def get_search_result_count(self):
        return len(self.driver.find_elements(*self.search_results))