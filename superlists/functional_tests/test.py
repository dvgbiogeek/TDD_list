from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(LiveServerTestCase):

    # Startup the browser
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # Shutdown the browser
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row_text for row in rows])

    def test_can_start_a_list_and_retrive_it_later(self):
        # Check out homepage
        self.browser.get(self.live_server_url)

        # Notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invite to-do item entries
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        
        # Enter to-do item
        inputbox.send_keys('Go for a walk')

        # Press enter and update the page showing the itemized to-do list
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Go for a walk')
        time.sleep(1)

        # Still have a text box for entering a new item.
        # Add another item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Pick up groceries for curry')
        inputbox.send_keys(Keys.ENTER)
        
        time.sleep(1)

        # Update page with first and second item.
        self.check_for_row_in_list_table('1: Go for a walk')
        self.check_for_row_in_list_table('2: Pick up groceries for curry')
        time.sleep(1)

        self.fail('Finish the test!')

if __name__ =='__main__':
    unittest.main(warnings='ignore')

