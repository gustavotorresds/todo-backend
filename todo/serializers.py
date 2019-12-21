from rest_framework import serializers

from .models import Goal, Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
	tasks = TaskSerializer(many=True, read_only=True, required=False)

	class Meta:
		model = Goal
		fields = '__all__'