from django.urls import path

from .views import CreateTokenView, CreateUserView

app_name = "accounts"

urlpatterns = [
    path("", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
]
