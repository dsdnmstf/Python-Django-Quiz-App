from django.urls import path
from .views import CategoryDetail, CategoryList

urlpatterns = [
path("", CategoryList.as_view(), name="category"),
path("<category>", CategoryDetail.as_view(), name="category-detail"),

]