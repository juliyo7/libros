from django.contrib import admin
from django.urls import path, include
from catalogo.views import lista_libros

urlpatterns = [
   path("admin/", admin.site.urls),
   path("", lista_libros),                 # ← raíz /
   path("libros/", include("catalogo.urls")),
]
