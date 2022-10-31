from django.db import models


class Task(models.Model):
	user = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
