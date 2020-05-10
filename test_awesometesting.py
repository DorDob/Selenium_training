import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_post_count():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com/')
    # Pobranie listy tytułów
    list_of_titles = browser.find_elements(By.CSS_SELECTOR,'.post-title.entry-title')

    # Asercja - lista ma 4 elementy
    #assert len(list_of_titles) == 4

def test_post_count_after_search():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com/')
    # Inicjalizacja searchbara i przycisku search
    search_bar = browser.find_element(By.CSS_SELECTOR,'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')
    # Szukanie
    search_bar.send_keys('cypress')
    search_button.click()
    # Czekanie na stronę
    time.sleep(5)
    # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')
    # Asercja że lista ma 3 elementy
    assert len(titles) == 3
    # Zamknięcie przeglądarki
    browser.close()


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony
    browser.get('https://www.awesome-testing.com/')
    # Inicjalizacja elementu z labelką
    label = browser.find_element(By.LINK_TEXT, 'Cypress')
    # Kliknięcie na labelkę
    label.click()
    # Czekanie na stronę
    time.sleep(5)
    # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, 'input.gsc-input')
    # Asercja że lista ma 1 element
    assert len(titles) == 1
    # Zamknięcie przeglądarki

    .close()
