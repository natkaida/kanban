from api.views import DetailTask, ListTask

from django.urls import path

urlpatterns = [
    path('tasks/', ListTask.as_view()),
    path('task/<str:pk>', DetailTask.as_view()),
]
