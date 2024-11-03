# Generated by Django 5.1.2 on 2024-10-29 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=60, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=160, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/featured_images/')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published'), ('ARCHIVED', 'Archived')], default='DRAFT', max_length=10)),
                ('views', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('canonical_url', models.URLField(blank=True, null=True)),
                ('robots', models.CharField(choices=[('INDEX, FOLLOW', 'Index, Follow'), ('NOINDEX, FOLLOW', 'No Index, Follow'), ('INDEX, NOFOLLOW', 'Index, No Follow'), ('NOINDEX, NOFOLLOW', 'No Index, No Follow')], default='INDEX, FOLLOW', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.category')),
                ('tags', models.ManyToManyField(blank=True, to='article.tag')),
            ],
        ),
    ]