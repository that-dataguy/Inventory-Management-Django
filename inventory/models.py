from django.db import models
from django.forms import ModelForm

# Create your models here.

class add_sale(models.Model):
    color = models.CharField(
        max_length = 10,
        choices=[
            ('White',"White"),
            ('Black',"Black"),
        ]
    )
    size = models.CharField(
        max_length = 3,
        choices=[
            ('S',"Small"),
            ('M',"Medium"),
            ('L',"Large"),
            ('XL',"Extra Large"),
        ]
    )
    quantity = models.PositiveIntegerField()
    invoice_number = models.CharField(max_length=10)
    date = models.DateField(auto_now = True)

class SaleForm(ModelForm):
    class Meta:
        model = add_sale
        fields = ["color", "size", "quantity", "invoice_number"]

class add_stock(models.Model):
    date = models.DateField(auto_now = True)
    color = models.CharField(
        max_length = 10,
        choices=[
            ('White',"White"),
            ('Black',"Black"),
        ]
    )
    size = models.CharField(
        max_length = 3,
        choices=[
            ('S',"Small"),
            ('M',"Medium"),
            ('L',"Large"),
            ('XL',"Extra Large"),
        ]
    )
    quantity = models.PositiveIntegerField()
    details = models.CharField(max_length = 50)
    

class StockForm(ModelForm):
    class Meta:
        model = add_stock
        fields = ["color", "size", "quantity", "details"]