from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student_register', views.student_register),
    path('login', views.login, name='login'),
    path('teacher_register', views.teacher_register),
    path('student_profile', views.student_profile, name="student_profile"),
    path('teacher_profile', views.teacher_profile, name="teacher_profile")
]