import pytest

from pages.home_page import HomePage
from pages.search_page import SearchPage
from utilities.csv_reader import CSVReader


products = CSVReader.read_products("data/test_data.csv")


@pytest.mark.parametrize("product", products)
def test_product_search(driver, product):

    driver.get("https://tutorialsninja.com/demo/")

    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    home_page.search_product(product)

    heading = search_page.get_search_heading()
    result_count = search_page.get_search_result_count()

    assert "Search" in heading
    assert result_count > 0