from django import forms
from django.core.validators import validate_integer
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class SavingForm(forms.Form):
    capital = forms.CharField(label='Initial Capital', validators=[RegexValidator(regex='^[1-9]\d*(\.\d+)?$')])
    years = forms.CharField(label='Number of Years', initial=5, validators=[RegexValidator(regex='^[1-9]\d*(\.\d+)?$')])
    interest = forms.CharField(label='Interest Rate (annual)', initial=3.5, validators=[RegexValidator(regex='^[0-9]\d*(\.\d+)?$')])

    def clean(self):
        cd=self.cleaned_data