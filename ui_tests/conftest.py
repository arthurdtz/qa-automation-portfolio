import os

import pytest
from selenium import webdriver


def _headless() -> bool:
    # Headless on CI (GitHub Actions sets CI=true) or when HEADLESS=1 is set locally
    return os.getenv("CI") == "true" or os.getenv("HEADLESS") == "1"


@pytest.fixture
def driver():
    # Setup Chrome WebDriver (Selenium Manager resolves the matching driver)
    options = webdriver.ChromeOptions()
    if _headless():
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    # Teardown
    driver.quit()
