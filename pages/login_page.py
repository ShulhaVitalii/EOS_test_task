import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    locators = LoginPageLocators()

    def log_in(self):
        email = 'shulha.vitalii.n@gmail.com'
        password = 'Pa$$w0rd'
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_clickable(self.locators.SIGN_IN_BUTTON).click()
        self.on_this_screen(self.locators.SIDEBAR_USER)
        assert self.driver.current_url == 'https://crop-monitoring.eos.com/main-map/fields/all'


