from django.urls import path

from .views import ArticleView

# app_name поможет выполнить обратный поиск.
app_name = "articles"


urlpatterns = [
    path('articles/', ArticleView.as_view({'get': 'list'})),
    path('articles/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
]