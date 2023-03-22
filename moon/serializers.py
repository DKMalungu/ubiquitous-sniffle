from rest_framework import serializers


class MovieDetailsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    director = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    rating = serializers.FloatField()
    description = serializers.CharField()
    image = serializers.ImageField()
    movie_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(default=True)


class StudentDetailsSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    middle_name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    address = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    student_id = serializers.IntegerField(read_only=True)
