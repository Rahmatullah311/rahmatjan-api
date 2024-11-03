from rest_framework import serializers
from .models import Article

class ArticleSerializer (serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = ('title', 'slug', 'summary')


class ArticleDetailsSerializer (serializers.ModelSerializer):
  class Meta:
    model = Article
    fields = '__all__'