import time

from pages.registration_page import RegistrationPage
from pages.gmail_page import GmailPage


class TestRegistrationPage:

    def test_registration(self, driver):
        registration_page = RegistrationPage(driver, 'https://crop-monitoring.eos.com/login')
        registration_page.open()
        registration_page.filling_out_the_form()
        confirm_code = registration_page.get_confirm_code()
        registration_page.enter_the_confirm_code(confirm_code)
        time.sleep(30)
