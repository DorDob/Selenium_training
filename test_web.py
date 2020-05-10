from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


                                    # Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
                                        # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
                                        # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())  # 1. sparwdza wersję przeglądarrkin 2. sprawdza czy jest driver pod tą przeglądarkę.
                                                                       # 3. Jeśli nie ma to ściąga driver 4. ustawia zmienną systemową do drivera
    browser.maximize_window()                                          # browser.fullscreen_window() a to druga metoda powiększenia okana na cały ekran

                                        # Otwarcie strony testareny - pierwsze użycie Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

                                        #    browser.find_element(By.NAME,'#Slawek')
                                        #    browser.find_element_by_css_selector("[name='heading'")

                                        # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in browser.title

                                        # Zamknięcie przeglądarki
    browser.quit()


                                        # Test - uruchomienie Firefoxa
def test_my_first_firefox_selenium_test():
                                        # Uruchomienie przeglądarki Firefox. Ścieżka do geckodrivera (drivera dla Firefoxa)
                                        # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Firefox(executable_path=GeckoDriverManager().install())

def test_my_first_google_slenium_test():
    browser = Chrome(executable_path=ChromeDriverManager().install())
                                        # Otwarcie strony www.google.pl
    browser.get('https://www.google.pl')
                                        # Weryfikacja tytułu
    assert browser.title == 'Google'    #dwa zapisy tej asercji
    assert 'Google' in browser.title
                                        # Zamknięcie przeglądarki
    browser.quit()
