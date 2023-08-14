from django import forms
from .models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:

        model = Profile
        exclude = ["picture", "age"]

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': ''
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["password", "email"]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Image URL',
            'age': 'Age'
        }
