from django.contrib import admin
from django.urls import path, include   # 👈 aquí agregamos include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("mi_app.urls")),   # 👈 esto ya está bien
]
