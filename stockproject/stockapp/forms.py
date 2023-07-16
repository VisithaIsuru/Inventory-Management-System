from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_code', 'item_brand','colour', 'size', 'category', 'quantity', 'price']