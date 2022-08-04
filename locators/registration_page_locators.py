from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    GO_TO_SIGN_UP_BUTTON = (By.XPATH, '//button[@data-id="go-signup-btn"]')

    FACEBOOK_BUTTON = (By.XPATH, '//div[@data-id="facebook-btn"]')
    GOOGLE_BUTTON = (By.XPATH, '//button[@data-id="google-btn"]')

    FIRSTNAME_INPUT = (By.XPATH, '//input[@data-id="first_name"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@data-id="last_name"]')
    EMAIL_INPUT = (By.XPATH, '//input[@data-id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-id="password"]')

    CHECKBOX = (By.XPATH, '//input[@id="mat-checkbox-1-input"]')
    MAT_CHECKBOX = (By.XPATH, '//mat-checkbox[@data-id="policy_confirm"]')

    TERMS_OF_USE_LINK = (By.XPATH, '//a[@data-id="terms-of-use"]')
    PRIVACY_POLICY_LINK = (By.XPATH, '//a[@data-id="privacy-policy"]')

    SIGN_UP_BUTTON = (By.XPATH, '//button[@data-id="sign-up-btn"]')


    # Verifacion page locators

    VERIFICATION_TEXT = (By.XPATH, '//h1[@class="title"]')

    EMAIL_TEXT = (By.XPATH, '//div[@class="email"]')

    CODE_INPUT = (By.XPATH, '//input[@data-id="confirm-code-input"]')

    SUBMIT_CODE_BUTTON = (By.XPATH, '//button[@data-id="submit-code-btn"]')
    RESENT_CODE_BUTTON = (By.XPATH, '//button[@data-id="resend-code-btn"]')
