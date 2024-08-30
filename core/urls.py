from django.urls import path
from .views import (
    lesson_list, lesson_create, lesson_update, lesson_delete,
    student_list, student_create, student_update, student_delete
)

urlpatterns = [
    path('', lesson_list, name='lesson_list'),
    path('lessons/new/', lesson_create, name='lesson_create'),
    path('lessons/<int:pk>/edit/', lesson_update, name='lesson_update'),
    path('lessons/<int:pk>/delete/', lesson_delete, name='lesson_delete'),

    path('students/', student_list, name='student_list'),
    path('students/new/', student_create, name='student_create'),
    path('students/<int:pk>/edit/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
]
