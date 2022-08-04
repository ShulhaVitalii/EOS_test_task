from pages.login_page import LoginPage


class TestLoginPage:

    def test_registration(self, driver):
        login_page = LoginPage(driver, 'https://crop-monitoring.eos.com/login/auth')
        login_page.open()
        login_page.log_in()
