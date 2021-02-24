import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print("\nInside Fixture driver. Opening Browser")
    driver = webdriver.Chrome(
        executable_path="D:\\Python-SeleniumAutomationFramework\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(20)

    yield driver

    print("\nInside Fixture driver. Closing Browser")
    driver.quit()
