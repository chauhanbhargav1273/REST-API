from django.db import models

# Create your models here.


class Faculty(models.Model):
	name=models.CharField(max_length=100,blank=True , default="")
	mobile=models.PositiveIntegerField(blank=True , default=0)
	email=models.EmailField(blank=True ,  default="")
	subject=models.CharField(max_length=100,blank=True,  default="")

	def __str__(self):
		return self.name

class Student(models.Model):
	name=models.CharField(max_length=100,blank=True ,  default="")
	mobile=models.PositiveIntegerField(blank=True , default=0)
	email=models.EmailField(blank=True , default="")
	subject=models.CharField(max_length=100,blank=True , default="")
	faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE, default='bhargav')

	def __str__(self):
		return self.name

