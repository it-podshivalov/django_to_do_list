from django.contrib import admin
from my_task.models import Tasks
from datetime import datetime


@admin.action(description="Done")
def done(modeladmin, request, queryset):
    queryset.update(completed=True, endTime=datetime.now())


@admin.action(description="Return to Work")
def return_to_work(modeladmin, request, queryset):
    queryset.update(completed=False, endTime=None)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "task",
        "creationTime",
        "endTime",
        "completed",
    ]
    search_fields = [("task")]
    actions = [done, return_to_work]
