from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('todolist/', views.todolist, name="todolist"),
    path('update/<int:pk>/', views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
