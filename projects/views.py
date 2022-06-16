"""
View definitions for the projects portion of the site
"""

from django.shortcuts import render
from projects.models import Project

# Create your views here.

APP = "projects"


def project_index(request):
    """List of projects

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    projects = Project.objects.all()
    context = {
        "app": APP,
        "projects": projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    """Project details

    Args:
        request ([type]): [description]
        pk ([type]): [description]

    Returns:
        [type]: [description]
    """
    project = Project.objects.get(pk=pk)
    context = {
        "app": APP,
        "project": project
    }

    return render(request, 'project_detail.html', context)
