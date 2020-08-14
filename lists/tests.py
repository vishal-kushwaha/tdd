from django.test import TestCase
from pytest_django.asserts import assertTemplateUsed


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


# pytest type tests
def test_home_page_returns_correct_html(client):
    response = client.get('/')
    assertTemplateUsed(response, 'lists/home.html')
