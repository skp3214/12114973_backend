from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_tasks, name='list_tasks'), 
    path('tasks/create/', views.add_task, name='create_task'), 
    path('tasks/<int:pk>/', views.get_task, name='get_task'), 
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'), 
    path('tasks/<int:pk>/update/', views.update_task, name='update_task'),
    path('tasks/bulk-add/', views.add_bulk_task, name='bulk_add_tasks'), 
    path('tasks/bulk-delete/', views.delete_bulk_task, name='bulk_delete_tasks'),  
]
