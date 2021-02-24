from selenium.webdriver.common.by import By


class GoogleHomePage:
    URL = "https://www.google.com"
    SEARCH_BOX = (By.NAME, 'q')
    FIRST_SUGGESTION_TEXT = (By.XPATH, ".//div[contains(@class,'suggestions-inner-container')]")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    def test_in_search_box(self, phrase):
        self.driver.find_element(
            self.SEARCH_BOX[0], self.SEARCH_BOX[1]).send_keys(phrase)

    def get_first_suggestion(self):
        return self.driver.find_element(*self.FIRST_SUGGESTION_TEXT).text
