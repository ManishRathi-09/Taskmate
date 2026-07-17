from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('complete/<task_id>', views.complete, name='mark_complete'),
    path('pending/<task_id>', views.pending, name='mark_pending'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>',views.edit_task, name='edit_task'),
 
]