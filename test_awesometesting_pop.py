import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.home import HomePage
from pages.search_result import SearchResultPage

def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.awesome-testing.com/')
    yield browser
    browser.quit()

def test_post_count(browser):
    home_page = HomePage(browser)
    home_page.verify_post_count(4)

def test_post_count_after_search(browser):
    home_page = HomePage(browser)
    home_page.search('cypress')

    search_result_page = SearchResultPage(browser)
    search_result_page.wait_for_load()

    search_result_page.verify_post_count(3)


    # Pobranie listy tytułów

    # Zamknięcie przeglądarki



def test_post_count_on_cypress_label(browser):

    home_page = HomePage(browser)
    home_page.label_click("Cypress")

    # Czekanie na stronę
    search_result_page = SearchResultPage(browser)
    search_result_page.wait_for_load()

    # Pobranie listy tytułów
    search_result_page.verify_post_count(1)

    # Zamknięcie przeglądarki
    browser.quit()
