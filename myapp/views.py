from django.shortcuts import render
from rest_framework import generics
from .models import Student,Faculty
from .serializers import StudentSerializer,FacultySerializer

# Create your views here.
class StudentList(generics.ListCreateAPIView):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Student
	serializer_class=StudentSerializer

class FacultyList(generics.ListCreateAPIView):
	queryset=Faculty.objects.all()
	serializer_class=FacultySerializer

class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Faculty
	serializer_class=FacultySerializer
