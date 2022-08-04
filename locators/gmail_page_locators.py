from selenium.webdriver.common.by import By


class GmailPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@id="identifierId"]')

    CONTINUE_BUTTON = (By.XPATH, '//div[@id="identifierNext"]//button[@type="button"]')

    PASSWORD_INPUT = (By.XPATH, '//input[@type="password"]')

    NEXT_BUTTON = (By.XPATH, '//div[@id="passwordNext"]//button[@type="button"]')

    LAST_MAIL = (By.XPATH, '//tbody/tr[@tabindex="-1"][1]')

    CODE = (By.XPATH, '//table/tbody/tr[12]/td/div/span')

