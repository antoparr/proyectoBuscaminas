from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tablero', views.form_tablero, name='tablero')
]