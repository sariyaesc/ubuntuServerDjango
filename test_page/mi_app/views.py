from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

tasks = ["foo","bar","baz"]  # lista en memoria

def index(request):
    return render(request, "mi_app/index.html")

def index2(request):
    return render(request, "mi_app/index2.html")

def tasks_index(request):
    return render(request,"mi_app/tasks_index.html", {"tasks": tasks})

def tasks_add(request):
    if request.method == "POST":
        task_text = request.POST.get("task")
        if task_text:
            tasks.append(task_text)
        return HttpResponseRedirect(reverse("tasks_index"))
    return render(request, "mi_app/tasks_add.html")

def tasks_admin_list(request):
    tasks = Task.objects.all().order_by("created_at")  # quitar el "_"
    return render(request, "mi_app/tasks_admin_list.html", {"tasks": tasks})

# Las otras vistas (index1, hello, current_datetime, greet, saludo, about, sumar) puedes dejarlas igual
