from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUser(TestCase):
    """
    Test custom User functionality.
    """

    def test_create_user(self):
        """
        Should create user with email and password.
        """
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
