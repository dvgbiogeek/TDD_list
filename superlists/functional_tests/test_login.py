import time

from .base import FunctionalTest

TEST_EMAIL = 'edith@mockmyid.com'

class LoginTest(FunctionalTest):

    def switch_to_new_window(self, text_in_title):
        retries = 30
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def test_login_with_persona(self):
        # Check for login link
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()
        # time.sleep(10)

        # A Persona login box appears
        self.switch_to_new_window('Mozilla Persona')
        time.sleep(2)

        # Login with email address - Use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # The Persona window closes
        self.switch_to_new_window('To-Do')

        # User is now logged in
        self.wait_to_be_logged_in(email=TEST_EMAIL)
        
        # User stays logged in with a page refresh
        self.browser.refresh()
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # Click logout
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

        # User still logged out after a refresh
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)



