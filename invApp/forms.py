
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'name',
            'sku',
            'price',
            'quantity',
            'supplier',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Product Name',
            }),

            'sku': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'SKU',
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Price',
                'min': '0',
                'step': '0.01',
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Quantity',
                'min': '0',
                'step': '1',
            }),

            'supplier': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white border-secondary',
                'placeholder': 'Supplier',
            }),
        }
