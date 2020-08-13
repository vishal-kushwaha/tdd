from django.test import TestCase
from pytest_django.asserts import assertTemplateUsed


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')


# pytest type tests
def test_home_page_returns_correct_html(client):
    response = client.get('/')
    assertTemplateUsed(response, 'lists/home.html')


def test_can_save_a_POST_request(client):
    response = client.post('/', {'item_text': 'A new list item'})
    assert 'A new list item' in response.content.decode()
    assertTemplateUsed(response, 'lists/home.html')
