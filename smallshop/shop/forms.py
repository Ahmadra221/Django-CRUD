from django import forms
from django.forms.widgets import NumberInput
from .models import Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
       
   