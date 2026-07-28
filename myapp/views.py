from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse("<h1>Projects</h1>")

def tasks(request):
    return HttpResponse("<h1>Tasks</h1>")