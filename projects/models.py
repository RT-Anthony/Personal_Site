"""
Models for projects portion of the site
"""

from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Data structure that defines a project

    Args:
        models ([type]): [description]
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')
