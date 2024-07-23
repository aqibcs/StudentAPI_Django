from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.list_student, name='list_student'),
    path('students/<int:pk>/', views.get_student, name='get_student'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/update/', views.update_student, name='update_student'),
    path('students/<int:pk>/partial-update/', views.partial_update_student, name='partial_update_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
]
