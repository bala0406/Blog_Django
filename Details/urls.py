from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "Details"

urlpatterns = [
    path("read/",views.read_details,name = "read"),
    path("create/",views.create_details,name="create"),
    path("update/",views.update_details,name = "update"),
    path("<str:name>/",views.detailed_view,name = "detail"),
    path("<str:deletename>/delete/",views.delete_details,name = "delete"),
    path("<str:updatename>/update/",views.update_details,name = "update"),
    path("",views.search_details,name = "search")
]