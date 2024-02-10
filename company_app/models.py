from django.db import models
from django.contrib.auth.models import User,Group,Permission
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,AbstractUser

# Create your models here
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

class JobList(models.Model):
    Job_id=models.AutoField(primary_key=True)
    published_date=models.DateTimeField()
    Job_name=models.CharField(max_length=200)
    Company_name=models.CharField(max_length=200)
    Company_Address=models.CharField(max_length=300)
    Company_Location=models.CharField(max_length=300,null=True,blank=True)
    Job_description=models.CharField(max_length=300)
    Salary_range1=models.CharField(max_length=200)
    Salary_range2=models.CharField(max_length=200)
    Job_type=models.CharField(max_length=200,choices=job_type,default='FullTime')
    Prefered_location=models.CharField(max_length=200,choices=prefered_location,default='Kerala')
    Experience_level=models.CharField(max_length=200,choices=Experience,default='Fresher')
    Apply_link=models.CharField(max_length=200)
    Qualification=models.CharField(max_length=200)
    Responsibility=models.CharField(max_length=200)
    last_date=models.DateTimeField()
    Vaccancy=models.CharField(max_length=200,default=1)
    Company_image=models.ImageField(null=True,blank=True,upload_to="jobs")






class Employee(models.Model):
    name=models.CharField(max_length=200)
    Phone_Number=models.IntegerField()
    Address=models.CharField(max_length=250)
    Designation=models.CharField(max_length=250)
    Profile_Image=models.FileField(upload_to="company",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)








       
