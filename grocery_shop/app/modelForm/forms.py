from django import forms
from app.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']