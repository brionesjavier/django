from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from myapp.models import Project,Task

# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request,username):
    print(f"saludos {username}")
    #forma antigua de concadenar
    return HttpResponse("<h2>Hello %s</h2>" % username)

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    tasks = get_object_or_404(Task,id=id)

    return HttpResponse(f"task: {tasks.title}")