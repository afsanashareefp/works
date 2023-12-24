from django.contrib import messages, auth
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render
from django.http import JsonResponse

from .forms import PersonCreationForm
from .models import Department, Course, Details


# Create your views here.

def allCourDep(request, c_slug=None):
    c_page = None
    course = None
    if c_slug != None:
        c_page = get_object_or_404(Department, slug=c_slug)
        course = Course.objects.all().filter(department=c_page, available=True)

    else:
        course = Course.objects.all().filter(available=True)

    return render(request, "department.html", {'department': c_page, 'course': course})


def courDep(request, c_slug, course_slug):
    try:
        course = Course.objects.get(department__slug=c_slug, slug=course_slug)
    except Exception as e:
        raise e
    return render(request, "course.html", {'course': course})


def details_form(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = PersonCreationForm()
    return render(request, 'details.html', {'form': form})



