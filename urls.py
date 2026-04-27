from django.urls import path

from . import views

urlpatterns = [
    path("", views.report_create, name="report_create"),
    path("admin-map/", views.admin_map, name="admin_map"),
]
