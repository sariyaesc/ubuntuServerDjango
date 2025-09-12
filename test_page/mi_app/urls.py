from django.urls import path
from . import views   # importa tu archivo views.py

urlpatterns = [
    path('', views.index, name='index'),  # http://localhost:8000/hello/ mostrará "Hello World!"
]