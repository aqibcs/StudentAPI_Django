from django.urls import path
from .views import create_student, list_student, get_student, update_student, partial_update_student, delete_student

urlpatterns = [
    path('', create_student),
    path('list', list_student),
    path('<int:pk>', get_student),
    path('update/<int:pk>', update_student),
    path('partial/<int:pk>', partial_update_student),
    path('delete/<int:pk>', delete_student)
]
