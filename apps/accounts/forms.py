
from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User

class RegisterUserForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "data_nascimento", "escolaridade")