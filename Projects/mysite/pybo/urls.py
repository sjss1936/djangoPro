from django.urls import path, include
from pybo import views

urlpatterns = [
    path('', views.index, name='index'),
]
