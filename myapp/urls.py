from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello,name="hello"),
    path('projects/', views.projects,name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks,name="tasks"),
    path('create_tasks/', views.create_tasks,name="create_tasks"),
    path('create_project/', views.create_projects,name="create_project"),
]
