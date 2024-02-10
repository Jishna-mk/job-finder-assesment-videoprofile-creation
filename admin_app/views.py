from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login,logout
from company_app.models import Employee
from django.shortcuts import get_object_or_404
from django.contrib import messages
# from company_app.models import EmployeeProfile
# Create your views here.

def admin_signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("view_dashboard")
        else:
            messages.info(request,"username or password incorrect")
            return redirect("admin_signin")

    return render(request,"admin/admin_signin.html")

def admin_signout(request):
    logout(request)
    return redirect("admin_signin")

def view_dashboard(request):
    company=Employee.objects.all().order_by("-id")
    return render(request,"admin/dashboard.html",{"company":company})

def approve(request,c_id):
    company = User.objects.get(id = c_id)
    company.is_active = True
    company.save()
    messages.success(request,"Approved as Manager")
    return redirect("view_dashboard")
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


def remove(request, c_id):
    try:
        company = get_object_or_404(User, id=c_id)
        employee_profile = Employee.objects.filter(user=company)

        if employee_profile.exists():
            employee_profile[0].delete()
        company.delete()

        messages.success(request, "Company Profile Removed")
    except Exception as e:
        print(f"Error removing company: {str(e)}")
        messages.error(request, "Error while removing company")

    return redirect("view_dashboard")
