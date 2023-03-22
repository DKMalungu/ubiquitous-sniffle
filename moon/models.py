from django.db import models


class MovieDetails(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.FloatField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/')
    movie_id = models.IntegerField(primary_key=True, auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class meta:
        table = 'movie_details'
        order = 'movie_id ASC'


class StudentDetails(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    student_id = models.IntegerField(primary_key=True, auto_created=True)

    class meta:
        table = 'student_details'
        order = 'first_name'
