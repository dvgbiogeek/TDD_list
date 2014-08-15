from selenium import webdriver
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
        self.fail('Finish the test!')

if __name__ =='__main__':
    unittest.main(warnings='ignore')

