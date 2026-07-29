from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index, name="home"),
    path("about/" , views.about,name="about"),
    path("hello/<str:username>", views.hello),
    path("projects/", views.projects,name="projects"),
    path("tasks/", views.tasks,name="tasks"),

]