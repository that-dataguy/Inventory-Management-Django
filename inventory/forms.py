from django.forms import ModelForm
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = ["color", "size", "total_quantity"]

class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ["item", "date"]