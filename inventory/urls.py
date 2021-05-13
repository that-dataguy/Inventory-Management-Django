from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    #path('salesreport', views.salesreport, name='sales_report'),
    path('add_sale', views.add_sale, name='addsale'),
    path('add_stock', views.add_stock, name='addstock'),
]
