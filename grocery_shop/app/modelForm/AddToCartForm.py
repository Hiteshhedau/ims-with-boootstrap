
from django import forms
from app.models import Cart

class AddToCartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['product','quantity']

