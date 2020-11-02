"""
View calls for the blog portion of the site
"""

from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.
def blog_index(request):
    """
    List all blog entries

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    """
    List the categories available for the blog
    Args:
        request ([type]): [description]
        category ([type]): [description]

    Returns:
        [type]: [description]
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    """
    Show an individual blog article
    Args:
        request ([type]): [description]
        pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)
