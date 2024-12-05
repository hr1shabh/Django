from django import forms
from .models import Cars

class CarsForm(forms.Form):
    car_variety = forms.ModelChoiceField(queryset=Cars.objects.all(), label='select car variety')