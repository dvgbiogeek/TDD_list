from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip
import time


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # Cannot submit an empty list item

        # Error message says list items cannot be blank

        # New item now works

        # Attempts are made for a second blank list submission

        # Again a similiar warning shows up

        # Text saves the day!

        self.fail('write me!')


if __name__ =='__main__':
    unittest.main(warnings='ignore')

