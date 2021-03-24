from django.shortcuts import render
from django.http import HttpResponse
from .models import Shirt

# Create your views here.
def index(request):
    return HttpResponse("Hello, You're at Picture This")

def salesreport(request):
    shirt_sales = Shirt.objects.all() 
    context = {'shirt_sales': shirt_sales} 
    return render(request, 'inventory/reports.html', context)