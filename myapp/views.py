from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Project, Task

from .forms import CreateNewTask

# Create your views here.


def index(request):
    title = "Django Course!!"
    return render(request, "index.html", {"title": title})


def hello(request, username):
    print(f"saludos {username}")
    # forma antigua de concadenar
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    return render(request, "about.html")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()

    return render(request, "tasks/tasks.html", {"tasks": tasks})


def create_task(request):

    if request.method == "GET":

        return render(request,
                      "tasks/create_task.html",
                      {"form": CreateNewTask})

    elif request.method == "POST":
        print(request.POST["title"])
        print(request.POST["description"])

        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )
        return redirect("tasks")
    else:
        print("metodo no permitidos")
