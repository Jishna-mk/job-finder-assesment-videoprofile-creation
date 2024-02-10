from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from  .import models as QMODEL

from .import forms as QFORM


# Create your views here.
def dashboard_view(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
   
    }
    return render(request,'company/dashboard.html',context=dict)


def exam_view(request):
    return render(request,'company/exam.html')


def add_exam(request):
    courseForm=QFORM.CourseForm()
    if request.method=='POST':
        courseForm=QFORM.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
        else:
            print("form is invalid")
        return redirect('view-exam')
    return render(request,'company/add_exam.html',{'courseForm':courseForm})


def view_exam(request):
    courses = QMODEL.Course.objects.all()
    return render(request,'company/view_exam.html',{'courses':courses})


def delete_exam(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    course.delete()
    return redirect('view-exam')


def question_view(request):
    return render(request,'company/question.html')

def add_question(request):
    questionForm=QFORM.QuestionForm()
    if request.method=='POST':
        questionForm=QFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=QMODEL.Course.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
        else:
            print("form is invalid")
        return redirect('view-question')
    return render(request,'company/add_question.html',{'questionForm':questionForm})

def view_question(request):
    courses= QMODEL.Course.objects.all()
    return render(request,'company/view_question.html',{'courses':courses})


def see_question(request,pk):
    questions=QMODEL.Question.objects.all().filter(course_id=pk)
    return render(request,'company/see_question.html',{'questions':questions})


def remove_question(request,pk):
    question=QMODEL.Question.objects.get(id=pk)
    question.delete()
    return redirect('view_question')
