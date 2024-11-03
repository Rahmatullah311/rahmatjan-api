from django.urls import path
from .views import Articles, ArticleDetail

urlpatterns = [
  path('article/', Articles.as_view(), name='articles'),
  path('article/<slug:slug>/', ArticleDetail.as_view(), name='article'),
]