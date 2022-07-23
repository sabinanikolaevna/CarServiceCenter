"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from tickets.views import welcome
from tickets.views import menu
from tickets.views import change_oil
from tickets.views import tiress
from tickets.views import diag
from tickets.views import processing
from django.views.generic import RedirectView
from tickets.views import next




urlpatterns = [
    path('welcome/', welcome),
    path('menu/', menu),
    path('get_ticket/change_oil', change_oil),
    path('get_ticket/inflate_tires', tiress),
    path('get_ticket/diagnostic', diag),
    path('processing', processing),
    path('processing/', RedirectView.as_view(url='/processing')),
    path('next', next)
]
