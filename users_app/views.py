from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from company_app.models import JobList
from  .forms import UserAddForm,AddUserForm
from .models import UserProfile,Message
from  exam_app import models as QMODEL
from exam_app import forms,models
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate, login
from  company_app.models import Employee
from .decorators import user_only
# Create your views here.
def home(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
 

def about(request):
    return render(request,"about.html")  
def category(request):
    return render(request,"category.html")

def testimonial(request):
    return render(request,"testimonial.html")    
  
              
from django.contrib.auth.models import Group
def job_list(request):
    jobs=JobList.objects.all().order_by("-Job_id")
    p=Paginator(jobs,5)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)        
    return render(request,"job-list.html",{"page_obj":page_obj})

def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            group = Group.objects.get(name='users')  # Get the "users" group
            user.groups.add(group)  # Add the user to the "users" group
            messages.info(request, "New User Created")
            return redirect('signin')
    return render(request, "signup.html", {"form": form})



def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("job_list")
        else:
            
            messages.info(request,"Username or Password Incorrect")
            return redirect("signin")

    return render(request,"signin.html")


def signout(request):
    
    logout(request)
    return redirect('home')

def job_details(request, Job_id):
    job = get_object_or_404(JobList, pk=Job_id)
    return render(request, 'job-detail.html', {'job': job})

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobList, JobApplication
from .forms import JobApplicationForm
from django.contrib.auth.decorators import login_required

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(JobList, pk=job_id)

    # Check if the user has created a profile
    user_profile = User.objects.filter(id=request.user.id).first()
    if not user_profile:
        messages.warning(request, "Please create a profile before applying for a job.")
        return redirect("create_profile")

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            messages.info(request, "Your application was submitted successfully.")
            return redirect('user_applications')  # Redirect to a success page or job list
    else:
        form = JobApplicationForm()

    return render(request, 'apply_job.html', {'form': form, 'job': job})

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def user_applications(request):
    user_applications = JobApplication.objects.filter(user=request.user).order_by('-application_date')
    return render(request, 'applied_jobs.html', {'user_applications': user_applications})

from .models import JobApplication

def withdraw_application(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)
    application.delete()
    return redirect('user_applications')


@login_required
def create_profile(request):
    form = AddUserForm()
    if request.method == "POST":
        add_form = AddUserForm(request.POST,request.FILES)
        if(add_form.is_valid()):
            user = User.objects.get(id=request.user.id)
            updated_profile = add_form.save()
            updated_profile.user_ID = user
            updated_profile.save()
            return redirect("view_user_profile")
    return render(request, "users/create_profile.html",{"form":form}) 


def view_user_profile(request):
    user = UserProfile.objects.filter(user_ID=request.user.id)
    if(len(user) == 0):
        return redirect("create_profile")
    return render(request,"users/user_profile.html",{"user":user[0]})



def student_dashboard(request):
    dict={
    
    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request,'users/student_dashboard.html',context=dict)


def student_exam(request):
    courses=QMODEL.Course.objects.all()
     # Check if the user has created a profile
    user_profile = User.objects.filter(id=request.user.id).first()
    if not user_profile:
        messages.warning(request, "Please create a profile before applying for a job.")
        return redirect("create_profile")
    return render(request,'users/student_exam.html',{'courses':courses})





def take_exam(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    total_questions = QMODEL.Question.objects.all().filter(course=course).count()
    questions = QMODEL.Question.objects.all().filter(course=course)
    total_marks = sum(q.marks for q in questions)

    return render(request, 'users/take_exam.html', {'course': course, 'total_questions': total_questions, 'total_marks': total_marks})




def start_exam(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    questions = QMODEL.Question.objects.all().filter(course=course)
    
    # Check if the user has created a profile
    user_profile = UserProfile.objects.filter(user_ID=request.user.id).first()
    if not user_profile:
        messages.warning(request, "Please create a profile before starting the exam.")
        return redirect("create_profile")

    if request.method == 'POST':
        # Handle the form submission here if needed
        pass
    
    response = render(request, 'users/start_exam.html', {'course': course, 'questions': questions})
    response.set_cookie('course_id', course.id)
    return response


# def calculate_marks(request):
#     if request.COOKIES.get('course_id') is not None:
#         course_id = request.COOKIES.get('course_id')
#         course=QMODEL.Course.objects.get(id=course_id)
        
#         total_marks=0
#         questions=QMODEL.Question.objects.all().filter(course=course)
#         for i in range(len(questions)):
            
#             selected_ans = request.COOKIES.get(str(i+1))
#             actual_answer = questions[i].answer
#             if selected_ans == actual_answer:
#                 total_marks = total_marks + questions[i].marks
#         student = models.UserProfile.objects.get( user_ID=request.user.id)
#         result = QMODEL.Result()
#         result.marks=total_marks
#         result.exam=course
#         result.student=student
#         result.save()

#         return redirect('view_result')

def calculate_marks(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        course = QMODEL.Course.objects.get(id=course_id)
        
        total_marks = 0
        questions = QMODEL.Question.objects.all().filter(course=course)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks += questions[i].marks
        
        student = models.UserProfile.objects.get(user_ID=request.user.id)
        result = QMODEL.Result()
        result.marks = total_marks
        result.exam = course
        result.student = student
        result.save()

        # Redirect to the view-result page
        return redirect('view-result')


def view_result(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'users/view_result.html', {'courses': courses})

def check_marks(request, pk):
    course = QMODEL.Course.objects.get(id=pk)
    student = models.UserProfile.objects.get(user_ID=request.user.id)
    results = QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
    return render(request, 'users/check_marks.html', {'results': results})

def student_marks(request):
    courses = QMODEL.Course.objects.all()
    return render(request, 'users/student_marks.html', {'courses': courses})

def video(request):
    return render(request,"camera.html")

def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'company/employee_list.html', {'employees': employees})

@user_only 
def send_message(request, id):
    if request.method == "POST":
        message = request.POST["message"]
        user = User.objects.get(id=id)
        company= Employee.objects.get(user=user)
        f = Message(message=message, company=company, user=request.user)
        f.save()
        messages.info(request, "Message Sent")
        return redirect("view_messages")
@user_only    
def view_messages(request):
    user_messages = Message.objects.filter(user=request.user).exclude(reply=True)
    reply_messages = Message.objects.filter(user=request.user).exclude(reply=False)
    user_messages_count = user_messages.count()
    reply_messages_count = reply_messages.count()
    return render(request, "users/view-messages.html",{"user_messages":user_messages,"reply_messages":reply_messages,"user_messages_count":user_messages_count,"reply_messages_count":reply_messages_count})    