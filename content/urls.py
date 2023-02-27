from django.urls import path
from content import views

urlpatterns = [

    path('', views.index, name='content-index'),
    path('contact/', views.contact, name='content-contact'),
    
]
