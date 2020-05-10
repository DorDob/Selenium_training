import random
import string
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from pages.login_page import LoginPage
from pages.waiting import Waiting


@pytest.fixture()
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('http://demo.testarena.pl/')
    yield browser
    browser.quit()


def test_arena(browser):

    # LOGUJĘ SIĘ DO  demo.testarena.pl

    login_page = LoginPage(browser)
    login_page.login('administrator@testarena.pl', 'sumXQQ72$L')

    # OTWIERAM ADMIN PANEL
    admin_button = browser.find_element_by_css_selector('.header_admin a')
    admin_button.click()

    # DODAJĘ NOWY PROJEKT
    button_links = browser.find_element_by_partial_link_text('DODAJ PROJEKT')
    button_links.click()

    name = browser.find_element_by_id('name')
    prefix = browser.find_element_by_id('prefix')
    save = browser.find_element_by_id('save')



    # UMIESZCZAM LOSOWO WYGENEROWANĄ NAZWĘ PROJEKTU W ZMIENNEJ - ZA POMOCĄ TEJ ZMIENNEJ BĘDĘ SZUKAĆ PROJEKTU W BAZIE

    name_of_project = get_random_string(10)    # name_of_project - MOJA ZMIENNA

    name.send_keys(name_of_project)
    prefix.send_keys(get_random_string(6))
    save.click()


    # WCHODZĘ DO SEKCJI PROJECTS (LEWE MENU)

    enter_the_section_projects = browser.find_element(By.CSS_SELECTOR,'a.activeMenu')
    enter_the_section_projects.click()

    # SZUKAM NOWO-UTWORZONEGO PROJEKTU PO NAZWIE

    search_for_new_project = browser.find_element(By.CSS_SELECTOR, 'input#search')
    search_for_new_project.send_keys(name_of_project)      # PASEK WYSZUKIWANIA

    button_for_search_new_project = browser.find_element(By.CSS_SELECTOR, 'a#j_searchButton.icon_search.icon-20')
    button_for_search_new_project.click()                  # PRZYCISK WYSZUKIWANIA (LUPA)


    # CZEKAM NA STRONĘ

    # wait = WebDriverWait(browser, 10)
    # grey_status_bar = (By.CSS_SELECTOR,'input#search')
    # wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))

    time_for_waiting = Waiting(browser)
    time_for_waiting.wait_for_loading()


    # TWORZĘ LISTĘ PROJEKTÓW W BAZIE

    projects = browser.find_elements(By.CSS_SELECTOR,'tr td a')


    # NASTĘPNIE, TWORZĘ KOLEJNĄ LISTĘ, KTÓRA BĘDZIE ZAWIERAĆ NAZWY TYCH PROJEKTÓW

    list_with_names = []

    for every_project in projects:
        list_with_names.append(every_project.text)


    # W ASERCJI SPRAWDZAM, CZY ZNAJDUJĄCA SIĘ W ZMIENNEJ NAZWA MOJEGO PROJEKTU - ZNAJDUJE SIĘ NA LIŚCIE NAZW STWORZONYCH PROJEKTÓW

    assert name_of_project in list_with_names
    print(name_of_project)



def get_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
