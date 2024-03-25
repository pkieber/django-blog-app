from django.urls import include, path
from .views import Featured, Index, DetailArticleView, LikeArticle

urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("", Index.as_view(), name="index"),
    path("<int:pk>/", DetailArticleView.as_view(), name="detail_article"),
    path("<int:pk>/like/", LikeArticle.as_view(), name="like_article"),
    path("featured/", Featured.as_view(), name="featured"),
]
