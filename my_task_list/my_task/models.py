from django.db import models
from django.urls import reverse
from datetime import datetime


class Tasks(models.Model):
    task = models.CharField(max_length=300)
    creationTime = models.DateTimeField(
        editable=False, auto_now_add=True, help_text="Время создания задачи"
    )
    endTime = models.DateTimeField(
        null=True, blank=True, default=None, help_text="Время завершения задачи"
    )
    completed = models.BooleanField(default=False, help_text="Выполнено")

    class Meta:
        ordering = ["-creationTime"]

    def get_absolute_url(self):
        return reverse("task", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        if self.completed:
            self.endTime = datetime.now()
            return super().save(*args, **kwargs)
        else:
            self.endTime = None
            return super().save(*args, **kwargs)

    def completed_text(self):
        if self.completed:
            return "Задача выполнена"
        else:
            return "Задача не выполнена"

    def __str__(self) -> str:
        return f"{self.task}"
