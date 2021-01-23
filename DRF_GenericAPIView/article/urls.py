from django.urls import path

from .views import ArticleView, SingleArticleView


app_name = "articles"

# app_name поможет нам выполнить обратный поиск..
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
]