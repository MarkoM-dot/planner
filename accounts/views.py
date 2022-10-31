from rest_framework import generics

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Create user api view.
    """

    serializer_class = UserSerializer
