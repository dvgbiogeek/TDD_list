from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrive_it_later(self):
        # Check out homepage
        self.browser.get(self.server_url)
        # time.sleep(10)
        # import pdb; pdb.set_trace()
        # Notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invite to-do item entries
        inputbox = self.get_item_input_box()
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        
        # Enter to-do item
        inputbox.send_keys('Go for a walk')

        # Press enter, redirect to a new URL with the page showing the itemized 
        # to-do list
        inputbox.send_keys(Keys.ENTER)
        
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Go for a walk')
        # time.sleep(2)

        # Still have a text box for entering a new item.
        # Add another item.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Pick up groceries for curry')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(2)
        # Update page with first and second item.
        self.check_for_row_in_list_table('1: Go for a walk')
        self.check_for_row_in_list_table('2: Pick up groceries for curry')

        # A new user comes to the site
        # We use a new browser session to make sure no other user's list shows - 
        # remove cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Go for a walk', page_text)
        self.assertNotIn('Pick up groceries for curry', page_text)

        # Enter new item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy eggplant')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(2)
        # Next user gets their own unique URL
        next_user_list_url = self.browser.current_url
        self.assertRegex(next_user_list_url, '/lists/.+')
        self.assertNotEqual(next_user_list_url, user_list_url)

        # Check for traces of other user's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Go for a walk', page_text)
        self.assertIn('1: Buy eggplant', page_text)
        # time.sleep(3)

if __name__ =='__main__':
    unittest.main(warnings='ignore')

