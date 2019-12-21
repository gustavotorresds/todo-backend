from rest_framework import generics, viewsets

from .models import Goal, Task
from .serializers import GoalSerializer, TaskSerializer

class GoalViewSet(viewsets.ModelViewSet):
	queryset = Goal.objects.all()
	serializer_class = GoalSerializer

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# class GoalList(APIView):
# 	def get(self, request):
# 		goals = Goal.objects.all()
# 		data = GoalSerializer(goals, many=True).data
# 		return Response(data)

# class GoalDetail(APIView):
	# def get(self, request, pk):
	# 	goal = get_object_or_404(Goal, pk=pk)
	# 	data = GoalSerializer(goal).data
	# 	return Response(data)

# class GoalList(generics.ListCreateAPIView):
# 	queryset = Goal.objects.all()
# 	serializer_class = GoalSerializer
	
# class GoalDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Goal.objects.all()
# 	serializer_class = GoalSerializer

# class TaskList(generics.ListCreateAPIView):
# 	queryset = Task.objects.all()
# 	serializer_class = TaskSerializer

# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Task.objects.all()
# 	serializer_class = TaskSerializer
