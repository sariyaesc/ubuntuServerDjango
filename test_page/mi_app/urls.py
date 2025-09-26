from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index1/", views.index1, name='index1'),
    path("hello/", views.hello, name='hello'),
    path("datetime/", views.current_datetime, name='datetime'),
    path("greet/<str:name>/", views.greet, name='greet'),
    path("about/", views.about, name='about'),
    path("sumar/", views.sumar, name='sumar'),
    path("<str:nombre>/", views.saludo, name='saludo'),  
]