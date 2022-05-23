from django.urls import path, include
from . import views
import asyncio

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("service/", views.services, name="services"),
    path("contact/", views.contacts, name="contacts"),

    # path("contact/success", views.contacts, name="success"),
    # path("contact/failure", views.contacts, name="failure"),
    path("about/", views.about, name="about"),
]
