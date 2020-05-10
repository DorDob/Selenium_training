from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera

    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony duckduckgo
    browser.get('https://duckduckgo.com/')
    # Znalezienie paska wyszukiwania
    search_form = browser.find_element(By.CSS_SELECTOR, '#search_form_input_homepage')

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element_by_id('search_button_homepage')

    # Asercje że elementy są widoczne dla użytkownika
    assert search_form.is_displayed()
    assert search_button.is_displayed() is True  # nie trzeba pisa is True, bo inaczej jak bedzie False to i tak test się wywali

    # Szukanie Vistula University
    search_form.send_keys('Vistula University')
    search_button.click()

    # Sprawdzenie że akikolwiek wynik ma tytuł 'Vistula University in Warsaw'
    list = browser.find_elements(By.CSS_SELECTOR, '.result__title')
    list_of_titles = []
    for i in list:
        list_of_titles.append(i.text)
    assert 'Vistula University in Warsaw' in list_of_titles
    assert list == 'Vistula University in Warsaw'


    # Zamknięcie przeglądarki

    browser.quit()
