from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.password_validation import validate_password


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
        
        validate_password(password)

        return cleaned_data


class UserProfileForm(ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_new_password=forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_new_password', 'first_name', 'last_name', 'avatar',]
    
    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        old_password = cleaned_data.get("old_password")
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password != confirm_new_password:
            self.add_error('confirm_new_password', "Password does not match")
        
        validate_password(new_password)

        return cleaned_data