from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Please enter your password'
        self.fields['password2'].help_text = 'I hope its not to much beer today, you will make it'
        self.fields['username'].help_text = 'Just be original'


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ("picture", )
