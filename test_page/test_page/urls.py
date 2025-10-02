from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("index2/", views.index2, name="index2"), 
    path("tasks/", views.tasks_index, name="tasks_index"),
    path("tasks/add/", views.tasks_add, name="tasks_add"),
    path("tasks/admin/", views.tasks_admin_list, name="tasks_admin_list"),
]
