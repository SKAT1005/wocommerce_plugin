from django import forms

from .models import API, Order


class APIForm(forms.ModelForm):
    class Meta:
        model = API
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['api', 'link', 'servis_id', 'quantity']