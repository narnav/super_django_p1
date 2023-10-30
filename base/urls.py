# appliactionnnnnnnnnnnnnnnnnnnnnnnnnnnn
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login/', TokenObtainPairView.as_view()),

]
