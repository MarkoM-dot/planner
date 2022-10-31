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

    def test_create_user_normalizes_email(self):
        """
        Email is normalized prior to creating a new user.
        """
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.com", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email, password="sample1234"
            )
            self.assertEqual(user.email, expected)

    def test_create_user_without_email_raises_error(self):
        """
        Raises error where we do not have an email.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="", password="test123")

    def test_create_superuser(self):
        """
        Create a super user.
        """
        user = get_user_model().objects.create_superuser(
            email="testsuper@example.com", password="test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
