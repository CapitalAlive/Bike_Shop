from django.forms.models import ModelForm
from . import models
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = []
        labels = {
            "name": "your name",
            "surname": "your surname",
            "phone_number": "your phone number",
            "status": "status",
            "bike": "bike",

        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['bike'].widget = forms.HiddenInput()
        self.fields['status'].widget = forms.HiddenInput()
