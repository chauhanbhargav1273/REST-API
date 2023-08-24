from django.contrib import admin
from django.urls import path
from myapp.views import FacultyList,FacultyDetail,StudentList,StudentDetail


urlpatterns = [
   path('students/',StudentList.as_view()),
   path('students/<int:pk>',StudentDetail.as_view()),
   path('facultys/',FacultyList.as_view()),
   path('facultys/<int:pk>',FacultyDetail.as_view()),
   path('admin/', admin.site.urls),
]