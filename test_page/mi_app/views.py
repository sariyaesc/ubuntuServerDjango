# views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def saludo(request):
    # Devuelve un saludo personalizado
    return HttpResponse("¡Hola, bienvenido a mi página!")

def despedida(request):
    # Devuelve un mensaje de despedida
    return HttpResponse("¡Adiós, que tengas un buen día!")
