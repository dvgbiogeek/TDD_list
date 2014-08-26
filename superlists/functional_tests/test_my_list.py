from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore

from .base import FunctionalTest

User = get_user_model()

class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()
        # to set a cookie, first visit a domain - 404 pages are fastest
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'

        self.browser.get(self.server_url)
        self.wait_to_be_logged_out(email)

        self.create_pre_authenticated_session(email)

        self.browser.get(self.server_url)
        self.wait_to_be_logged_in(email)

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Log in user
        self.create_pre_authenticated_session('edith@example.com')

        # go to home page and start a list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Reticulate splines\n')
        self.get_item_input_box().send_keys('Immanentize eschaton\n')
        first_list_url = self.browser.current_url

        # There is now a "My Lists" link
        self.browser.find_element_by_link_text('My lists').click()

        # Your list is in there, named according to the first item
        self.browser,find_element_by_link_text('Reticulate splines').click()
        self.assertEqual(self.browser.current_url, first_list_url)

        # You decide to start a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Click cows\n')
        second_list_url = self.browser.current_url

        # Under 'my lists', the new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('Click cows').click()
        self.assertEqual(self.browser.current_url, second_list_url)

        # You logout. The 'my lists' option disappears
        self.browser.find_element_by_id('id_logout').click()
        self.assertEqual(self.browser.find_element_by_link_text('My lists'), [])

