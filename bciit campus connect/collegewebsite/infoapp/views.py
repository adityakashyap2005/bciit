from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request,'infoapp/home.html')
#view for faculty info

def faculty_info(request):
    faculty_data = {
        'faculties': [
            {'name': '	Mr. Alok Mishra', 'department': 'Computer Science', 'email': '	alok@bciit.ac.in'},
            {'name': 'Ms Kritika', 'department': 'CSE', 'email': 'kritika@bciit.ac.in'},
            {'name': '	Ms. Sonia Batra', 'department': 'CSE', 'email': 'sonia@bciit.ac.in'}
        ]
    }
    return render(request, 'infoapp/faculty.html', faculty_data)


#view for student info

def student_info(request):
    students = [
        {'name': 'Aditya Kashyap', 'roll': '02211102023', 'course': 'BCA'},
        {'name': 'Aditi', 'roll': '02711102023', 'course': 'bCA'},
        {'name': 'Swati joshi', 'roll': '0711102023', 'course': 'BCA'},
    ]
    return render(request, 'infoapp/student.html', {'students': students})
