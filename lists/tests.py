from django.test import TestCase
from pytest_django.asserts import assertTemplateUsed

from lists.models import Item


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


# pytest type tests
def test_home_page_returns_correct_html(client):
    response = client.get('/')
    assertTemplateUsed(response, 'lists/home.html')


def test_can_save_a_POST_request(client):
    response = client.post('/', {'item_text': 'A new list item'})
    assert 'A new list item' in response.content.decode()
    assertTemplateUsed(response, 'lists/home.html')


def test_saving_and_retrieving_items(db):
    first_item = Item()
    first_item.text = 'The first (ever) list item'
    first_item.save()

    second_item = Item()
    second_item.text = 'Item the second'
    second_item.save()

    saved_items = Item.objects.all()
    assert saved_items.count() == 2

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    assert first_saved_item.text == 'The first (ever) list item'
    assert second_saved_item.text == 'Item the second'
