from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


# pytest type tests
def test_root_url_resolves_to_home_page_view():
    found = resolve('/')
    assert found.func == home_page
