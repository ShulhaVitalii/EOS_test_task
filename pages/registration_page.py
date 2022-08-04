import time

from generator.generators import generated_person
from locators.gmail_page_locators import GmailPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    locators = RegistrationPageLocators()
    google_locators = GmailPageLocators()
    email = BasePage.get_email_for_junk()

    def filling_out_the_form(self):
        person_info = next(generated_person())
        firstname = person_info.firstname
        lastname = person_info.lastname
        password = 'Passw0rd'

        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(self.email)
        self.element_is_visible(self.locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_clickable(self.locators.MAT_CHECKBOX).click()
        time.sleep(3)
        self.element_is_clickable(self.locators.SIGN_UP_BUTTON).click()
        self.checking_login_confirm_page()
        time.sleep(10)

    def checking_login_confirm_page(self):
        verification_text = self.element_is_visible(self.locators.VERIFICATION_TEXT)
        verification_email = self.element_is_visible(self.locators.EMAIL_TEXT).text
        assert verification_text
        assert verification_email == self.email

    def get_confirm_code(self):
        email = 'vitalii.autotest@gmail.com'
        password = 'Pa$$w0rd_vitalii.autotest'

        self.gmail_sign_in(email, password)
        time.sleep(1)
        self.element_is_visible(self.google_locators.LAST_MAIL).click()
        time.sleep(2)
        confirm_code = self.elements_are_visible(self.google_locators.CODE)[-1].text
        self.driver.switch_to.window(self.driver.window_handles[0])
        return confirm_code

    def gmail_sign_in(self, email, password):
        self.open_new_tab()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://mail.google.com/mail')
        self.element_is_visible(self.google_locators.EMAIL_INPUT).send_keys(email)
        self.element_is_clickable(self.google_locators.CONTINUE_BUTTON).click()
        self.element_is_visible(self.google_locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_clickable(self.google_locators.NEXT_BUTTON).click()

    def enter_the_confirm_code(self, code):
        self.element_is_present(self.locators.CODE_INPUT).send_keys(code)
        time.sleep(7)
        self.checking_that_it_is_main_page()

    def checking_that_it_is_main_page(self):
        assert self.driver.current_url == 'https://crop-monitoring.eos.com/main-map/fields/all'

