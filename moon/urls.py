from django.urls import path
from .views import movie_list, movie_detail, student_list, student_detail

urlpatterns = [
    path('movie_list/', movie_list, name='movie_list'),
    path('movie/<int:pk>/', movie_detail, name='movie_detail'),
    path('student_list/', student_list, name='student_list'),
    path('student/<int:pk>/', student_detail, name='student_detail'),

]
