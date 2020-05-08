from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CourseForm, SubscriptionForm
from .models import Course, Section, Subscription


def index(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            number  = form.cleaned_data['number']
            return HttpResponseRedirect(f'/{subject}/{number}')
    else:
        form = CourseForm()

    return render(request, 'pounce/index.html', {
        'form' : form
    })


def course_sections(request, subject, number):
    subject = subject.upper()
    number = number.upper()

    course = get_object_or_404(Course, subject=subject, number=number)
    section_list = Section.objects.filter(course=course)

    print(course)
    print(section_list)

    return render(request, 'pounce/course_sections.html', {
        'course'       : course,
        'section_list' : section_list,
    })


def subscribe(request, subject, number, sectionName):
    subject = subject.upper()
    number = number.upper()
    sectionName = sectionName.upper()

    course  = get_object_or_404(Course, subject=subject, number=number)
    section = get_object_or_404(Section, course=course, name=sectionName)

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=Subscription(section=section))
        if form.is_valid():
            form.save()
            return HttpResponse('subscribed! check your email.')
    else:
        form = SubscriptionForm()

    return render(request, 'pounce/subscription.html', {
        'section' : section,
        'form' : form
    })
