"""
admin settings for the django site
"""

from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """
    Blog post admin model
    """
    pass

class CategoryAdmin(admin.ModelAdmin):
    """
    Blog category admin model
    """
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
