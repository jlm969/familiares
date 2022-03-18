from django.urls import path
from appfamilia.views import *
from appfamilia import views


urlpatterns = [
     path('personas/', views.per),
     path('', views.inicio),
]
