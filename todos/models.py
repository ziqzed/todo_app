from django.db import models


class Task(models.Model):
	task_description = models.CharField(max_length=200)