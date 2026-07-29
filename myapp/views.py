from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from myapp.models import Project,Task

# Create your views here.

def index(request):
    title= "Django Course!!"
    return render(request, "index.html",{"title":title})

def hello(request,username):
    print(f"saludos {username}")
    #forma antigua de concadenar
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return render(request, "projects.html",{"projects":projects})

def tasks(request):
    tasks = Task.objects.all()

    return render(request, "tasks.html",{"tasks":tasks})