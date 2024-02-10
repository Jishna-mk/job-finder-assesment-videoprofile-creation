from django import forms
from .models import JobList
from django import forms
# from .models import Employee
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django.forms import TextInput,Textarea,NumberInput,DateInput
from .models import Employee

from django.utils.translation import gettext_lazy as _

class CustomImageWidget(forms.ClearableFileInput):
    clear_checkbox_label = ''

class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobList 
        fields = '__all__'

    
    widgets = {
            'your_image_field': CustomImageWidget,
            
        }  


class CompanyProfileForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name","Phone_Number","Designation","Address","Profile_Image"]

        widgets = {
            'name':TextInput(attrs={"class":"form-control","placeholder":"Company Name"}),
            'Phone_Number': TextInput(attrs={"class":"form-control","placeholder":"Enter Phone number"}),
            'Designation': TextInput(attrs={"class":"form-control","placeholder":"Enter  Your Designation"}),
            'Address': Textarea(attrs={"class":"form-control","placeholder":"Enter  Address"}),
            
        }
