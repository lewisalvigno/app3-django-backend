"""daf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from agents.views import RegisterAPI, PaiementAPI
from agents.views import agent_list, agent_specific, parking_list, parking_specific, paiement_list, paiement_specific
from knox import views as knox_views
from agents.views import LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('pay/', PaiementAPI.as_view(), name='pay'),
    path('login', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('agents/<int:id>', agent_specific),
    path('agents/', agent_list),
    path('parkings/', parking_list),
    path('parkings/<int:id>', parking_specific),
    path('paiements/', paiement_list),
    path('paiements/<int:id>', paiement_specific),



]
