from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salesreport', views.salesreport, name='sales_report'),
    path('addsale', views.addsale, name='addsale'),
]
