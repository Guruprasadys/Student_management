from django.contrib import admin
from .models import Course, Student, Attendance, Grade

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Grade)
