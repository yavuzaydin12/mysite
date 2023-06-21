from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("myprojects", views.myprojects, name="myprojects"),
    path("myproject1", views.myproject1, name="myproject1")

]