"""my_task_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_task.views import TaskListView
from my_task.views import TaskCreateView
from my_task.views import TaskUpdateView
from my_task.views import TaskDetailView
from my_task.views import TaskDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create/", TaskCreateView.as_view()),
    path("task/update/<slug:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("", TaskListView.as_view(), name="tasks"),
    path("task/<slug:pk>/", TaskDetailView.as_view(), name="task"),
    path("task/delete/<slug:pk>/", TaskDeleteView.as_view(), name="task_delete"),
]
