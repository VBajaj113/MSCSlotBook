from django import forms
from django.forms import ModelForm, PasswordInput
from .models import *


class BookingForm(ModelForm):
    class Meta:
        model = BookRequest
        fields = ['slot', 'reason']

class SlotDate(ModelForm):
    date = forms.DateField()
    class Meta:
        model = BookRequest
        fields = ['date']