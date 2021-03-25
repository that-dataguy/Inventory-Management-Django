from django.db import models
from django.forms import ModelForm

# Create your models here.

class Shirt(models.Model):
    sale_date = models.DateField()
    shirt_size = models.CharField(
        max_length = 2,
        choices=[
            ('S',"Small"),
            ('M',"Medium"),
            ('L',"Large"),
            ('XL',"Extra Large")
        ]
    )
    quantity = models.IntegerField()

class ShirtForm(ModelForm):
    class Meta:
        model = Shirt
        fields = ['sale_date','shirt_size', 'quantity']