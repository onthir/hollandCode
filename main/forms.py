from django import forms
from .models import *

# initialization form
class InitializeForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('full_name', 'email')