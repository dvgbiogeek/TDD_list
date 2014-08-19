from .base import FunctionalTest
import time


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        # Go to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # Check that inputbox is centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,
            512,
            delta=5
        )

        # Input is also centered
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,
            512,
            delta=5
        )


if __name__ =='__main__':
    unittest.main(warnings='ignore')

