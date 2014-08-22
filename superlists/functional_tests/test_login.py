import time
from selenium.webdriver.support.ui import WebDriverWait

from .base import FunctionalTest


class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
            lambda b: b.find_element_by_id(element_id)
        )

    def test_login_with_persona(self):
        # Check for login link
        self.browser.get(self.server_url)
<<<<<<< HEAD
        self.browser.find_element_by_id('id_login').click()
=======
        self.browser.find_element_by_id('login').click()
>>>>>>> FETCH_HEAD

        # A Persona login box appears
        self.switch_to_new_window('Mozilla Persona')

        # Login with email address - Use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # User is now logged in
<<<<<<< HEAD
        self.wait_for_element_with_id('id_logout')
=======
        self.wait_for_element_with_id('logout')
>>>>>>> FETCH_HEAD
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)
        time.sleep(2)