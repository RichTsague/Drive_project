from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),   # URL pour le panneau d'administration
    path('', include('drive.urls')),    # Inclure les URLs de l'application 'drive'
]
