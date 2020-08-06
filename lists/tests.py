from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))


# pytest type tests
def test_root_url_resolves_to_home_page_view():
    found = resolve('/')
    assert found.func == home_page


def test_home_page_returns_correct_html():
    request = HttpRequest()
    response = home_page(request)
    html = response.content.decode('utf8')
    assert html.startswith('<html>') and html.endswith('</html>')
    assert '<title>To-Do lists</title>' in html
