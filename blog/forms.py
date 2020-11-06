"""
Forms related to the blog portion of the site
"""

from django import forms

class CommentForm(forms.Form):
    """
    Form that is used for submitting a comment on the blog posts
    """
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
