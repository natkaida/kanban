from django.urls import path
from api.views import ListTask, DetailTask

urlpatterns = [
    path('tasks/', ListTask.as_view()),
    path('task/<str:pk>', DetailTask.as_view()),
]