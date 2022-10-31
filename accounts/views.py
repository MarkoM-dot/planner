from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import AuthTokenSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    """
    Create user api view.
    """

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    Generate a new token for auth user.
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
