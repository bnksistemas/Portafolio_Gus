from django.shortcuts import render
from .models import Course, Experience, Skill

# Create your views here.
def about(request):
    experiences = Experience.objects.all()
    courses = Course.objects.all()
    skils = Skill.objects.all()
    data = {
        'experiences': experiences, 
        'courses': courses,
        'skils': skils,
    }
    return render(request, 'about/about.html', data)