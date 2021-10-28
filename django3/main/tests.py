from django.test import TestCase

class HomepageTest(TestCase):

    def test_homepage_ok(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)