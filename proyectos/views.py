from django.shortcuts import render
from .models import Project
# Create your views here.
def projects(request):
    projects = Project.objects.all() 
    data = {
        'projects': projects
    }
    return render(request, 'proyectos/projects.html', data)
