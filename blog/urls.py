from django.urls import include, path
from .views import Index, DetailArticleView

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("", Index.as_view(), name="index"),
    path("<int:pk>/", DetailArticleView.as_view(), name="detail_article"),
]
