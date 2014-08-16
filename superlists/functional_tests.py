from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    # Startup the browser
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    # Shutdown the browser
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Check out homepage
        self.browser.get('http://localhost:8000')

        # Notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').header_text
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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Go for a walk' for row in rows)
        )
        
        # Still have a text box for entering a new item
        self.fail('Finish the test!')

if __name__ =='__main__':
    unittest.main(warnings='ignore')

