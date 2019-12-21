from django.urls import path

from rest_framework.routers import DefaultRouter
from .apiviews import GoalViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'goals', GoalViewSet, basename='goals')

urlpatterns = []
urlpatterns += router.urls

# from .apiviews import GoalList, GoalDetail, TaskList, TaskDetail
# urlpatterns += [
# 	path('tasks/', TaskList.as_view(), name='tasks_list'),
# 	path('tasks/<int:pk>/', TaskDetail.as_view(), name='tasks_detail'),
# 	path('goals/', GoalList.as_view(), name='goals_list'),
# 	path('goals/<int:pk>/', GoalDetail.as_view(), name='goals_detail'),
# ]
