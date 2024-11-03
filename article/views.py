from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, ArticleDetailsSerializer
from rest_framework.permissions import AllowAny

class Articles (APIView):
  permission_classes = [AllowAny]
  def get(self, request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)
  
  
class ArticleDetail (APIView):
  permission_classes = [AllowAny]
  def get(self, request, slug):
    article = get_object_or_404(Article, slug=slug)
    serializer = ArticleDetailsSerializer(article)
    return Response(serializer.data)