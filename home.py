from selenium.webdriver.common.by import By
class HomePage:

    def search(self, search_term):
        search_bar = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-input')
        search_button = self.browser.find_element(By.CSS_SELECTOR, 'input.gsc-search-button')
        search_bar.send_keys(search_term)
        search_button.click()



    def __init__(self, browser):
        self.browser = browser

    def verify_post_count(self, expected_count):
        list_of_post_titles = self.browser.find_elements(By.CSS_SELECTOR,'.post-title.entry-title')

        assert len(list_of_post_titles) == expected_count     # Asercja że lista ma 4 elementy

    def label_click(self, label_name):
        label = self.browser.find_element(By.LINK_TEXT, label_name)
        label.click()