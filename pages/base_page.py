from time import time



from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @classmethod
    def get_email_for_junk(cls):
        timestamp = int(time())
        return f'vitalii.autotest+{timestamp}@gmail.com'

    def on_this_screen(self, *args, timeout=None):
        timeout = timeout or self.driver.desired_capabilities['timeouts']['implicit']
        for locator in args:
            try:
                self.element_is_visible(locator, timeout)
            except :
                raise Exception(f'Failed to find {locator[1]} in {timeout} seconds')

    def open_new_tab(self):
        self.driver.execute_script("window.open(''),'_blannk'")
        self.driver.switch_to.window(self.driver.window_handles[1])
