from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.Hoopflix, name = "Hoopflix"),
    path("home/", views.Home, name = "Home"),
    path("portfolio/", views.Portfolio, name = "Portfolio"),
    path("contacts/", views.Contacts, name = "Contacts")
]
