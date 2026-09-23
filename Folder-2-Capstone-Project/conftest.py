import os
import pytest

from utilities.driver_factory import DriverFactory


@pytest.fixture
def driver():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = (
                f"{item.name}.png"
            )

            screenshot_path = os.path.join(
                "screenshots",
                screenshot_name
            )

            driver.save_screenshot(
                screenshot_path
            )

            print(
                f"\nScreenshot saved: "
                f"{screenshot_path}"
            )