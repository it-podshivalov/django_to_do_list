from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from my_task.models import Tasks
from django.contrib import messages


class TaskListView(ListView):
    context_object_name = "tasks"
    model = Tasks
    queryset = Tasks.objects.all()
    template_name = "tasks_list_view.html"


class TaskDetailView(DetailView):
    model = Tasks
    context_object_name = "task"
    template_name = "task_detail_view.html"


class TaskCreateView(CreateView):
    model = Tasks
    fields = ["task"]
    template_name = "task_create_view.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ["task", "completed", "endTime"]
    template_name = "task_update_view.html"
    success_url = "/"
    queryset = Tasks.objects.all()


class TaskDeleteView(DeleteView):
    model = Tasks
    context_object_name = "task"
    success_url = "/"
    template_name = "task_delete_view.html"
