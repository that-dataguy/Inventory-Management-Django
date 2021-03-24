from django.db import models

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

    def __str__ (self):
        return f"{self.shirt_size} ({self.id})"