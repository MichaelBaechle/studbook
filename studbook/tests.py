from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from studbook.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homepage_returns_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(str(response.content).startswith('<html>'))
        self.assertIn(
            '<title>Studbook: Social Networking for Dogs</title>',
            response.content)
        self.assertTrue(str(response.content).endswith('</html>'))
