from django import forms

from .models import Cleaner


class CleanerForm(forms.ModelForm):
    class Meta:
        model = Cleaner
        fields = ['first_name', 'last_name', 'quality_score', 'towns']
        widgets = {
            'towns': forms.CheckboxSelectMultiple()
        }
