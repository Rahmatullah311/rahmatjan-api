from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
    ARCHIVED = 'ARCHIVED'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
        (ARCHIVED, 'Archived'),
    ]

    INDEX_FOLLOW = 'INDEX, FOLLOW'
    NOINDEX_FOLLOW = 'NOINDEX, FOLLOW'
    INDEX_NOFOLLOW = 'INDEX, NOFOLLOW'
    NOINDEX_NOFOLLOW = 'NOINDEX, NOFOLLOW'
    ROBOTS_CHOICES = [
        (INDEX_FOLLOW, 'Index, Follow'),
        (NOINDEX_FOLLOW, 'No Index, Follow'),
        (INDEX_NOFOLLOW, 'Index, No Follow'),
        (NOINDEX_NOFOLLOW, 'No Index, No Follow'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='articles/featured_images/', blank=True, null=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    canonical_url = models.URLField(blank=True, null=True)
    robots = models.CharField(max_length=20, choices=ROBOTS_CHOICES, default=INDEX_FOLLOW)

    def __str__(self):
        return self.title
