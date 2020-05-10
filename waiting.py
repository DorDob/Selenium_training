
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def self(args):
    pass

class Waiting:

    def __init__(self, browser):
        self.browser = browser

    def wait_for_loading(self):
        wait = WebDriverWait(self.browser, 10)
        grey_status_bar = (By.CSS_SELECTOR, 'input#search')
        wait.until(expected_conditions.visibility_of_element_located(grey_status_bar))