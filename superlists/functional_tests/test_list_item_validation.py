from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):

        # Cannot submit an empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # Error message says list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # New item now works
        self.get_item_input_box().send_keys('Buy cilantro\n')
        self.check_for_row_in_list_table('1: Buy cilantro')

        # Attempts are made for a second blank list submission
        self.get_item_input_box().send_keys('\n')

        # Again a similiar warning shows up
        self.check_for_row_in_list_table('1: Buy cilantro')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # Text saves the day!
        self.get_item_input_box().send_keys('Make coffee\n')
        self.check_for_row_in_list_table('1: Buy cilantro')
        self.check_for_row_in_list_table('2: Make coffee')

    def test_cannot_add_duplicate_items(self):
        # Go to the home page and start a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy coffee\n')
        self.check_for_row_in_list_table('1: Buy coffee')

        # Enter duplicate item
        self.get_item_input_box().send_keys('Buy coffee')

        # Show helpful error with duplicated list item
        self.check_for_row_in_list_table('1: Buy coffee')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this on your list")
        # self.fail('write me!')

    def test_error_messages_are_cleared_on_input(self):

        # The user starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # Typing into the input box clears the error
        self.get_item_input_box().send_keys('a')
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())


if __name__ =='__main__':
    unittest.main(warnings='ignore')

