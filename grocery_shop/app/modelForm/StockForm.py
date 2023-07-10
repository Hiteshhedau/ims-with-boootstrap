from django import forms
from app.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product',  'qty_left']