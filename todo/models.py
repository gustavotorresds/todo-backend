from django.db import models

# Create your models here.
class Goal(models.Model):
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Task(models.Model):
	description = models.CharField(max_length=200)
	goal = models.ForeignKey(Goal, related_name="tasks", on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.description
