import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.awesome-testing.com/') 
    cookie = {'name': 'displayCookieNotice',
              'value': 'y',
              'domain': 'www.awesome-testing.com'}
    browser.add_cookie(cookie)
    browser.refresh()

    yield browser
    browser.quit()

def test_post_count(browser):
                                            # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
                                            # ustawiana automatycznie przez bibliotekę webdriver-manager
                                       
                                            # Pobranie listy tytułów
    list_of_titles = browser.find_elements(By.CSS_SELECTOR,'.post-title.entry-title')

                                            # Asercja że lista ma 4 elementy
                                            # assert len(list_of_titles) == 4
    assert len(list_of_post) == 4        
                                       
                                            # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
                                            # ustawiana automatycznie przez bibliotekę webdriver-manager
def test_post_count_after_search(browser):

                                            # Otwarcie strony - browser.get('https://www.awesome-testing.com/')
                                            # Inicjalizacja searchbara i przycisku search
    search_bar = browser.find_element(By.CSS_SELECTOR,'input.gsc-input')
    search_button = browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')
                                            # Szukanie
    search_bar.send_keys('cypress')
    search_button.click()
                                            # Czekanie na stronę  time.sleep(5)
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))
                                            # Pobranie listy tytułów
    titles = browser.find_elements(By.CLASS_NAME, 'post-title')
                                            # Asercja że lista ma 3 elementy
    assert len(titles) == 3                                         
                                            # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
                                            # ustawiana automatycznie przez bibliotekę webdriver-manager
def test_post_count_on_cypress_label(browser):
    

                                             # Otwarcie strony
                                             # browser.get('https://www.awesome-testing.com/')
                                             # Inicjalizacja elementu z labelką
    label = browser.find_element(By.LINK_TEXT, 'Cypress'                                     

    label.click()
                                              # Czekanie na stronę
    wait = WebDriverWait(browser, 10)
    grey_status_bar = (By.CLASS_NAME, 'status-msg-body')
    wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

                                              # Pobranie listy tytułów
    titles = browser.find_elements(By.CSS_SELECTOR, 'input.gsc-input')
                                              # Asercja że lista ma 1 element
    assert len(titles) == 1
                                              # Zamknięcie przeglądarki
    browser.quit()
