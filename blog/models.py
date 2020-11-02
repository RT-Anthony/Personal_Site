"""
Data models for the blog portion of the site
"""

from django.db import models

# Create your models here.
class Category(models.Model):
    """
    Category model for organizing, filering, and searching blog posts
    """
    name = models.CharField(max_length=20)

class Post(models.Model):
    """
    Blog post model for keeping post information
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
