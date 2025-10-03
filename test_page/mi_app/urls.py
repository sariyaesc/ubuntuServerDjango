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
    
    path("tasks/", views.tasks_index, name="tasks_index"),
    path("tasks/add/", views.tasks_add, name="tasks_add"),
    path("admin-tasks/", views.tasks_admin_list, name="tasks_admin_list"),
    path("index2/", views.index2, name="index2"),

    # Esta debe ir al final para no capturar rutas fijas
    path("<str:nombre>/", views.saludo, name='saludo'),  
]
