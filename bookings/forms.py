from django import forms

from .models import Booking
from towns.models import Town


class BookingForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    towns = forms.ModelChoiceField(queryset=Town.objects.all())

    class Meta:
        model = Booking
        fields = ['date']
