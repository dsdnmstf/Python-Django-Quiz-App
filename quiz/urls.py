from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("nested_admin/", include("nested_admin.urls") )
]