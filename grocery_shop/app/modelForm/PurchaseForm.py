from django import forms
from app.models import Purchase
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity', 'purchase_price', 'vender']