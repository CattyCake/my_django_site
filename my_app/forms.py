from django import forms
from .models import Order


class PostForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_name', 'courier', 'order_number')
