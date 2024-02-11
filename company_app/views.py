from django.shortcuts import render,redirect
from .models import JobList
from django.shortcuts import render, get_object_or_404
from .forms import JobDetailsForm ,CompanyProfileForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from users_app.forms import UserAddForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from users_app.models import JobApplication
from users_app.models import Message

# Create your views here.
def company_job_list(request):
    jobs=JobList.objects.all().order_by("-Job_id")
    p=Paginator(jobs,5)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)        
    return render(request,"company/company_joblist.html",{"page_obj":page_obj})   

# def company_joblist(request):
#     jobs=JobList.objects.all().order_by("-Job_id")
#     return render(request,"job-list.html",{'all_jobs':jobs})

def company_job_details(request, Job_id):
    job = get_object_or_404(JobList, pk=Job_id)
    return render(request, 'company/company-job-detail.html', {'job': job})

job_type=(
    ('PartTime','PartTime'),
    ('FullTime','FullTime'),
)
prefered_location=(
    ('Kerala','Kerala'),
    ('Bengaluru','Bengaluru'),
    ('Chennai','Chennai'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
)
Experience=(
    ('Internship','Internship'),
    ('Trainee','Trainee'),
    ('Fresher','Fresher'),
    ('Experienced','Experienced'),
)


def post_job(request):
    if request.method == 'POST':
        form = JobDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            job=form.save(commit=False) 
            job.save()
            form.save_m2m()
            messages.info(request, "Successfully Added")
            return redirect('job_list')
        else:
            messages.error(request,"Form validation failed")
    else:
        form = JobDetailsForm()

    return render(request, "add_jobs.html", {'form': form, 'job_type': job_type, 'prefered_location': prefered_location, 'Experience': Experience})


def deletejob(request,pk):
    edit=JobList.objects.get(Job_id=pk)
    edit.delete()
    messages.info(request,"deleted")
    return redirect("job_list")


def edit_job(request, pk):
    job = JobList.objects.get(Job_id=pk)
    if request.method == 'POST':
        form = JobDetailsForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully Edited")
            return redirect('company_job_list')
        else:
            messages.error(request, "Form validation failed")
    else:
        form = JobDetailsForm(instance=job)

    return render(request, "company/edit_job.html", {'form': form, 'job_type': job_type, 'prefered_location': prefered_location, 'Experience': Experience})

def companysignup(request):
    form = UserAddForm()
    company_form = CompanyProfileForm()

    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is Already Exists")
                return redirect('companysignup')
            if User.objects.filter(email=email).exists():
                messages.info(request, "This Emailid is Already Taken")
                return redirect('companysignup')

            new_user = form.save()
            new_user.is_active = False
            new_user.save()

            group = Group.objects.get(name='company')
            new_user.groups.add(group)

            company_form = CompanyProfileForm(request.POST, request.FILES)
            if company_form.is_valid():
                company = company_form.save(commit=False)
                company.user = new_user
                company.save()
                messages.success(request, "Registered as Company. Wait for Approval")
                return redirect('company_signin')
            else:
                messages.error(request, "Error in company profile details.")
        else:
            messages.error(request, "Error in user registration details.")
            # Add the following line to print form errors to the console for debugging
            print(form.errors)
    
    return render(request, "company/signup.html", {"form": form, "company_form": company_form})
def company_signin(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['password']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            messages.info(request,'Logged In Successfully')
            login(request, user1)
            group = request.user.groups.all()[0].name
            if(group == "company"):
                return redirect('company_job_list')
            else:
                messages.info(request,'Username or Password Incorrect')
                return redirect("company_signout")
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('company_signin')
    return render(request,"company/signin.html")


def company_signout(request):
    logout(request)
    return redirect('home')

def all_applications(request):
    all_applications = JobApplication.objects.all().order_by('-application_date')
    return render(request, 'company/all_applications.html', {'all_applications': all_applications})


from django.shortcuts import render, get_object_or_404
from users_app.models import UserProfile

def view_applicant(request, id):
    user = get_object_or_404(UserProfile, user_ID=id)
    return render(request, "company/user_profile.html", {"user": user})


# from django.shortcuts import render, get_object_or_404
# from users_app.models import JobApplication

# def view_application(request, application_id):
#     if request.user.is_authenticated:
#         user_application = get_object_or_404(JobApplication, id=application_id, user=request.user)
#         return render(request, 'company/view_application_details.html', {'user_application': user_application})
#     else:
#         return redirect('all_applications')

# def view_user_application(request, application_id):
#     user_application = get_object_or_404(JobApplication, id=application_id, user=request.user)
#     return render(request, 'company/view_application.html', {'user_application': user_application})


def video_cam(request):
    return render(request,"company/video.html")

from django.contrib.auth.decorators import login_required
from .models import Employee

@login_required
def employee_profile_view(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'company/employee_profile.html', {'employee': employee})



def send_message_to_user(request):
    if request.method == "POST":
        company = get_object_or_404(Employee, user=request.user)
        user_id = request.POST.get("user_id")  # Assuming you have a hidden input with user_id in your form
        user = get_object_or_404(User, id=user_id)
        message_text = request.POST["message"]

        # Create a new message with reply set to False for new messages to users
        Message.objects.create(message=message_text, company=company, user=user, reply=False)

        messages.info(request, "Message Sent")
        return redirect("view_messages")

    # Handle GET requests or other cases
    return redirect("view_messages")


def view_company_messages(request):
    company = get_object_or_404(Employee, user=request.user)
    user_messages = Message.objects.filter(company=company, reply=False)
    reply_messages = Message.objects.filter(company=company, reply=True)
    user_messages_count = user_messages.count()
    reply_messages_count = reply_messages.count()
    return render(request, "company/view-messages.html", {
        "user_messages": user_messages,
        "reply_messages": reply_messages,
        "user_messages_count": user_messages_count,
        "reply_messages_count": reply_messages_count
    })

def reply_message(request, id):
    if request.method == "POST":
        company = get_object_or_404(Employee, user=request.user)
        user = get_object_or_404(User, id=id)
        message_text = request.POST["message"]

        # Create a new message with reply set to True for user's sent messages
        Message.objects.create(message=message_text, company=company, user=user, reply=True)

        messages.info(request, "Message Sent")
        return redirect("view_messages")
