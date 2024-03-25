from django.urls import include, path
from .views import Index

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("", Index.as_view(), name="index"),
]
