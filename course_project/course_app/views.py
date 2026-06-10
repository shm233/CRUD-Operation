from django.shortcuts import render, redirect
from course_app.models import *

# Create your views here.

def course_view(request):
    course = CourseModel.objects.all()
    context = {
        'course':course
    }
    return render(request, 'home.html', context)

def course_add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        mark = request.POST.get('mark')
        department = request.POST.get('department')
        course_image = request.FILES.get('course_image')
        print("image:", course_image)
        start_date = request.POST.get('start_date')
        
        CourseModel.objects.create(
            title = title,
            mark = mark,
            department = department,
            course_image = course_image,
            start_date = start_date
        )
        return redirect('course_view')
    
    return render(request, 'add-courses.html')

def course_edit(request, c_id):
    course = CourseModel.objects.get(id = c_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        mark = request.POST.get('mark')
        department = request.POST.get('department')
        course_image = request.POST.get('course_image')
        start_date = request.POST.get('start_date')
        
        course.title = title
        course.mark = mark
        course.department = department
        if course_image:
            course.course_image = course_image
        course.start_date = start_date
        course.save()
        return redirect('course_view')
    
    context = {
        'course': course
    }
    return render(request, 'edit-course.html', context)

def course_delete(request, c_id):
    CourseModel.objects.get(id = c_id).delete()
    return redirect('course_view')
