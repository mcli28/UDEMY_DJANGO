from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Course

def index(request):
    courses = Course.objects
    return render(request, 'courses/index.html', {'courses': courses})
    
def detail(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/detail.html', {'course': course_detail})