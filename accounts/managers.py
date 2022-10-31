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

    def create_superuser(self, email, password):
        """
        Create a superuser.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
