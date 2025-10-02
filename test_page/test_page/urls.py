from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("mi_app.urls")), 
    path("index2/",include("mi_app.urls")),  
    path("tasks/", include("mi_app.urls")),
    path("tasks/add/", include("mi_app.urls")),
    path("tasks/admin/",include("mi_app.urls"))
]
 
