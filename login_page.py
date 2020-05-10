
class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, email, password):

        login_field = self.browser.find_element_by_id('email')
        password_field = self.browser.find_element_by_id('password')
        button_login = self.browser.find_element_by_id('login')
        login_field.send_keys(email)
        password_field.send_keys(password)
        button_login.click()



