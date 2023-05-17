from account.views import ResgisterUser
from django.urls import path

urlpatterns = [
    path("register", ResgisterUser.as_view(), name="register-user"),
]
