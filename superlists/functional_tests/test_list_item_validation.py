from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # Cannot submit an empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # Error message says list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # New item now works
        self.get_item_input_box().send_keys('Buy cilantro\n')
        self.check_for_row_in_list_table('1: Buy cilantro')

        # Attempts are made for a second blank list submission
        self.get_item_input_box().send_keys('\n')

        # Again a similiar warning shows up
        self.check_for_row_in_list_table('1: Buy cilantro')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # Text saves the day!
        self.get_item_input_box().send_keys('Make coffee\n')
        self.check_for_row_in_list_table('1: Buy cilantro')
        self.check_for_row_in_list_table('2: Make coffee')

        # self.fail('write me!')


if __name__ =='__main__':
    unittest.main(warnings='ignore')

