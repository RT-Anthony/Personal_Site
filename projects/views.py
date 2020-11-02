from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    """List of projects

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    projects = Project.objects.all()
    context = {
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
        'project': project
    }

    return render(request, 'project_detail.html', context)
