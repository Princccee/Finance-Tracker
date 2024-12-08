from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name")
    email = forms.EmailField(required=True, help_text="Enter a valid email address")
    phone_number = forms.CharField(max_length=15, required=True, help_text="Enter your phone number")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']