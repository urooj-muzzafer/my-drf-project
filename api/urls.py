from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('tasks/', views.taskList, name="taskList"),
    path('tasks/<str:pk>', views.taskDetail, name='taskDetail'),
]

