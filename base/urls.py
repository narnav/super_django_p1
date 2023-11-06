# appliactionnnnnnnnnnnnnnnnnnnnnnnnnnnn

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('members', views.member_only ),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('products', views.Product_view.as_view()),
    path('categories', views.Category_view.as_view()),
    path('order', views.OrderView.as_view()),

    
]




