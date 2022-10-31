from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Management methods for the custom User model.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a user with at least an email and password.

        Returns said user.
        """
        if not email:
            raise ValueError("You must provide an email.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
