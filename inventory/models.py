from django.db import models
from django.forms import ModelForm

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=10)
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
    #class Meta:
        #sequence = ('id','shirt_color','shirt_size','quantity','sale_date')

class ShirtForm(ModelForm):
    class Meta:
        model = Product
        fields = ['color','size', 'quantity']