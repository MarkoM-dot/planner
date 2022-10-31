from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

CREATE_USER_URL = reverse("accounts:create")
TOKEN_URL = reverse("accounts:token")


def create_user(**params):
    """
    Create a user.
    """
    return get_user_model().objects.create_user(**params)


class AnonymousUserApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Kitchen sink.
        """
        cls.User = get_user_model()
        cls.payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "first_name": "Testy",
            "last_name": "McTestorson",
        }

    def test_create_user_success(self):
        """
        Create a user.
        """
        res = self.client.post(CREATE_USER_URL, data=self.payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = self.User.objects.get(email=self.payload["email"])
        self.assertTrue(user.check_password(self.payload["password"]))
        self.assertEqual(user.first_name, self.payload["first_name"])
        self.assertEqual(user.last_name, self.payload["last_name"])
        self.assertNotIn("password", res.data)

    def test_user_with_email_exists_error(self):
        """
        Error returned if user with provided email already exists.
        """
        create_user(**self.payload)
        res = self.client.post(CREATE_USER_URL, self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password(self):
        """
        Bad password returns 400 and does not create a user.
        """
        payload = {
            "email": "example@example.com",
            "password": "pw",
        }
        res = self.client.post(CREATE_USER_URL, data=payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = self.User.objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_create_user_token(self):
        """
        Generates token for authentication.
        """
        user_details = {
            "first_name": "Testy",
            "last_name": "McTesterson",
            "email": "testonitis@example.com",
            "password": "test-user2413",
        }
        create_user(**user_details)

        payload = {
            "email": user_details["email"],
            "password": user_details["password"],
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_error(self):
        """
        Returns error if malformed request.
        """
        create_user(email="test@example.com", password="goodpass1")

        payload = {"email": "test@example.com", "password": "badpass"}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_empty_password(self):
        """
        An empty string password returns an error.
        """
        payload = {"email": "test@example.com", "password": ""}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
