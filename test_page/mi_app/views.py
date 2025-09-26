from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Task

def index1(request):
    return HttpResponse("<h1>Hello World!</h1>")

def hello(request):
    return HttpResponse("<h1>Hello desde la vista hello!</h1>")

def current_datetime(request):
    now = datetime.now()
    html = f"<h1>Fecha y hora actual:</h1><p>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>"
    return HttpResponse(html)

def greet(request, name):
    return HttpResponse(f"<h1>Hola, {name}!</h1>")

def saludo(request, nombre):
    return render(request, "mi_primera_pagina/saludo.html", {"nombre": nombre.capitalize()})

def index(request):
    return render(request, "mi_primera_pagina/index.html")

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page of the site.</p>")

def sumar(request):
    num1 = 5
    num2 = 3
    resultado = num1 + num2
    return render(request, 'mi_primera_pagina/sumar.html', {
        'num1': num1,
        'num2': num2,
        'resultado': resultado
    })