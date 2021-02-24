import time

from pages.googleHomePage import GoogleHomePage


def test_google_suggestion(driver):
    phrase = 'page object model'

    # Go to Google.com
    home_page = GoogleHomePage(driver)

    # Type text in search box
    home_page.test_in_search_box(phrase)
    time.sleep(1)
    # verify suggestions contains phrase
    suggestions = home_page.get_first_suggestion()
    time.sleep(1)
    assert phrase in suggestions
