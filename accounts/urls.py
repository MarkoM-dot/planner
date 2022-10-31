from django.urls import path

from .views import CreateUserView

app_name = "accounts"

urlpatterns = [
    path("", CreateUserView.as_view(), name="create"),
]
