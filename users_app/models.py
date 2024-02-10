from django.db import models
from django.contrib.auth.models import User
from company_app.models import JobList
from company_app.models import Employee
# Create your models here.



class JobApplication(models.Model):
    EXPERIENCE_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-3', '1-3 years'),
        ('3-5', '3-5 years'),
        ('5+', '5+ years'),
    ]

    QUALIFICATION_CHOICES = [
        ('BSC', 'BSc'),
        ('BBA', 'BBA'),
        ('Btech', 'B.Tech'),
        ('MBA', 'MBA'),
        ('MCA', 'MCA'),
        ('MSC', 'MSC'),
        ('Mtech', 'M.Tech'),
        ('Diploma', 'Diploma'),
        ('ITI', 'ITI'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobList, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    profile_picture=models.ImageField(null=True,blank=True,upload_to="jobs")
    email = models.EmailField()
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)  # Adjust the max_length as needed
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    experience = models.CharField(max_length=5, choices=EXPERIENCE_CHOICES)
    skills = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.Job_name} Application"

   


class UserProfile(models.Model):
    user_ID = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    User_Name = models.CharField(max_length=200,null=True,blank=True)
    Phone_Number = models.CharField(max_length=200,null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    Age = models.CharField(max_length=200,null=True,blank=True)
    User_photo = models.FileField(upload_to="users",null=True,blank=True)   


class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    company=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True)
    added_Date = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=200,null=True,blank=True)
    reply = models.BooleanField(default=False)    