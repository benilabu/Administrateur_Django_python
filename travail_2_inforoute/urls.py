"""travail_2_inforoute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path

from app_name.views import (
        Accueil,
        home_page_base,
        Accueil,
        Gestion_utilisateur,
        
)

    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_base, name="home"),
    path('Accueil', Accueil, name="Accueil"),
    path('Gestion_utilisateur', Gestion_utilisateur, name="Gestion_utilisateur"),
    
]
