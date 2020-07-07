from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("get_infos", views.get_infos, name="get_infos"),
    path("get_all", views.get_all, name="get_all"),
    path("get_past", views.get_past, name="get_past"),
    path("add_infos", views.add_infos, name="add_infos"),
]
