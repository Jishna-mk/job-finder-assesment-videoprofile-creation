from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
import re
from django.forms import TextInput,ModelForm,DateInput
from .models import UserProfile

class UserAddForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Your password must contain at least 8 characters, including letters, numbers, and symbols.",
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = User
        fields = ["first_name", "username", "email", "password1", "password2"]

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            raise ValidationError(
                "Your password must contain at least 8 characters, including letters, numbers, and symbols."
            )
        return password

from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'email', 'profile_picture', 'location', 'contact', 'qualification', 'experience', 'skills']

    def clean_resume(self):
        resume = self.cleaned_data['resume']

        # Check if the file extension is not PDF
        if not resume.name.lower().endswith('.pdf'):
            raise forms.ValidationError('Only PDF files are allowed for the resume.')

        return resume
     

class AddUserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["User_Name","Phone_Number","Address","Age","User_photo"]

        widgets = {
            'User_Name': TextInput(attrs={"class":"contact-input"}),
            'Phone_Number': TextInput(attrs={"class":"contact-input"}),
            'Address': TextInput(attrs={"class":"contact-input"}),
            'Age': TextInput(attrs={"class":"contact-input"}),
        }         