from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def explicit_wait(driver, locator, condition, time_to_wait):
    if condition == 'clickable':
        WebDriverWait(driver, time_to_wait).until(
            ec.element_to_be_clickable(locator))
