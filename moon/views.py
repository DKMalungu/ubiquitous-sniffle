from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieDetailsSerializer, StudentDetailsSerializer
from .models import MovieDetails, StudentDetails
from django.shortcuts import render

@api_view()
def movie_list(request):
    movies = MovieDetails.objects.all()
    serializer = MovieDetailsSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movie = MovieDetails.objects.get(pk=pk)
    serializer = MovieDetailsSerializer(movie)
    return Response(serializer.data)

@api_view()
def student_list(request):
    student = StudentDetails.objects.all()
    s_students = StudentDetailsSerializer(student, many=True)
    return Response(s_students.data)

@api_view()
def student_detail(request, pk):
    student = StudentDetails.objects.get(pk=pk)
    serializer = StudentDetailsSerializer(student)
    return Response(serializer.data)

