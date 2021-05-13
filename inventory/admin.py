from django.contrib import admin

# Register your models here.
from .models import add_sale, add_stock
admin.site.register(add_sale)
admin.site.register(add_stock)