from django.urls import path
from . import views

urlpatterns = [
    
 
    path('', views.c_dash),
    path('api/', views.getData, name="customer-list"),
    
    
    path('api/add/', views.addCustomer, name="add_customers"),
    
    path('api/delete/<str:pk>/', views.deleteCustomer, name ="Delete-Customer"),
    path('api/update/<str:pk>/', views.updateCustomer, name ="Update-Customer"),
    
    
    
    
]