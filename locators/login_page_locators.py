from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//button[@data-id="sign-in-button"]')

    EMAIL_INPUT = (By.XPATH, '//input[@data-id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-id="password"]')

    SIGN_IN_BUTTON = (By.XPATH, '//button[@data-id="sign-in-btn"]')

    SIDEBAR_USER = (By.XPATH, '//button[@data-id="sidebar-user-menu"]')
