from django.shortcuts import render
from .models import Student, Attendance, Grade

def home(request):
    return render(request, 'home.html')

def student_dashboard(request):
    # Example: show attendance and grades for logged-in student
    student = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=student)
    grades = Grade.objects.filter(student=student)
    return render(request, 'student_dashboard.html', {'attendance': attendance, 'grades': grades})

