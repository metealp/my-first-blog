from django.urls import path
from . import views

urlpatterns = [
    #======TODO_URLs======
    #CREATE 
    path('todo/add_todo/', views.add_todo_view, name='add_todo'),
    #RETRIEVE
    path('', views.todo_list_view, name='todo_list'),
    #UPDATE
    #DELETE
    path('todo/delete_todo/<int:pk>/', views.delete_todo, name='delete_todo')
]