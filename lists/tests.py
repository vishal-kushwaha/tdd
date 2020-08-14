import pytest
from django.test import TestCase
from pytest_django.asserts import assertTemplateUsed

from lists.models import Item


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class HomePageTest(TestCase):
    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


# pytest type tests
@pytest.mark.django_db
def test_home_page_returns_correct_html(client):
    response = client.get('/')
    assertTemplateUsed(response, 'lists/home.html')


@pytest.mark.django_db
def test_can_save_a_POST_request(client):
    response = client.post('/', {'item_text': 'A new list item'})

    assert Item.objects.count() == 1
    new_item = Item.objects.first()
    assert new_item.text == 'A new list item'


@pytest.mark.django_db
def test_redirects_after_POST(client):
    response = client.post('/', {'item_text': 'A new list item'})
    assert response.status_code == 302
    assert response['location'] == '/'


@pytest.mark.django_db
def test_saving_and_retrieving_items():
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


@pytest.mark.django_db
def test_only_saves_items_when_necessary(client):
    client.get('/')
    assert Item.objects.count() == 0


@pytest.mark.django_db
def test_displays_all_list_items(client):
    Item.objects.create(text='itemey 1')
    Item.objects.create(text='itemey 2')

    response = client.get('/')

    assert 'itemey 1' in response.content.decode()
    assert 'itemey 2' in response.content.decode()
