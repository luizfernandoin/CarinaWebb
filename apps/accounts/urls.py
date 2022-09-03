from django.urls import path
from .views import registerView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", registerView, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]