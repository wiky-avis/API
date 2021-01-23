# from django.urls import path

# from .views import ArticleView

# # app_name поможет выполнить обратный поиск.
# app_name = "articles"


# urlpatterns = [
#     path('articles/', ArticleView.as_view({'get': 'list'})),
#     path('articles/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
# ]

#класс DefaultRouter позволяет значительно уменьшить код в URL
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')
urlpatterns = router.urls