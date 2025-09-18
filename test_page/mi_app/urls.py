from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # http://localhost:8000/hello/
    path('saludo/', views.saludo, name='saludo'), # http://localhost:8000/hello/saludo/
    path('despedida/', views.despedida, name='despedida'), # http://localhost:8000/hello/despedida/
]
