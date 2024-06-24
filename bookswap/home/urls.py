from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('create', views.create_view, name='create'),
    path('sid', views.sid, name='sid'),
    path('gargi', views.gargi, name='gargi'),
    path('Input', views.Input, name='Input'),
    path('cart', views.cart, name='cart'),
    path('Ramcharitramanas', views.Ramcharitramanas, name='Ramcharitramanas'),
]