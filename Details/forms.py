from django import forms
from .models import UserInformation

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ["name","about","email","phone","gender"]