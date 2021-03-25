from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shirt, ShirtForm
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("Hello, You're at Picture This")

def salesreport(request):
    shirt_sales = Shirt.objects.all() 
    context = {'shirt_sales': shirt_sales} 
    return render(request, 'inventory/reports.html', context)

def addsale(request):
    if request.method == 'POST':
        form = ShirtForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ShirtForm()

    return render(request, 'inventory/sale.html', {'form': form})