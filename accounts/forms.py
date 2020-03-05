
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# registration form
class RegistrationForm(UserCreationForm):

    # extend from the User class
    class Meta:
        model = User

        # define fields for the form
        fields = ('username', 'email', 'password1', 'password2')