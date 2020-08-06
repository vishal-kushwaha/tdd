from django.test import TestCase


# unittest type tests based on Django's builtin test tools
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)


# pytest type tests
def test_smoke_test():
    assert 1 + 1 == 3
