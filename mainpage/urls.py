from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='index'),
    
    path('update/<int:pk>/', views.update_business, name='update_business'),
    
    path('business/', views.business_list, name='business_list'),
    path('business/create/', views.create_business, name='create_business'),
    
    path('performance/', views.performance_list, name='performance_list'),
    path('performance/create/', views.create_performance, name='create_performance'),
 

]