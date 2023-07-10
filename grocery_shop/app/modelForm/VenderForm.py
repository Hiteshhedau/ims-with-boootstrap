from django import forms
from app.models import Vender

class VenderForm(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ['name','email','address','phone_number']