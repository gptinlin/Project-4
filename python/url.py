from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('main.html', views.home, name="home" ),
    path('about.html', views.about, name="about" ),
    path('add_stock.html', views.add_stock, name="add_stock" ),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
    path('chart.html', views.chart, name="chart"),
    path('plots.html', views.tickplot, name="plots"),
    
] 