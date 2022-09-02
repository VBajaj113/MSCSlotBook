from django import forms
from django.forms import ModelForm, PasswordInput
from .models import *


class BookingForm(ModelForm):

    class Meta:
        model = Slot
        fields = ['date', 'start_time', 'end_time']
