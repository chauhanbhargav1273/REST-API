from rest_framework import serializers
from .models import Student,Faculty



class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student
		fields=('id','name','mobile','email','subject','faculty')

class FacultySerializer(serializers.ModelSerializer):
	class Meta:
		model=Faculty
		fields=('id','name','mobile','email','subject')
