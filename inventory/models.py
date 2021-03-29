from django.db import models
from django.forms import ModelForm

# Create your models here.

class Shirt(models.Model):
    shirt_color = models.CharField(
        max_length = 10,
        choices=[
            ('White',"White"),
            ('Black',"Black"),
        ]
    )
    shirt_size = models.CharField(
        max_length = 3,
        choices=[
            ('S',"Small"),
            ('M',"Medium"),
            ('L',"Large"),
            ('XL',"Extra Large"),
        ]
    )
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField(auto_now=True)
    
    #class Meta:
        #sequence = ('id','shirt_color','shirt_size','quantity','sale_date')

class ShirtForm(ModelForm):
    class Meta:
        model = Shirt
        fields = ['shirt_color','shirt_size', 'quantity']