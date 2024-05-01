from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from app_blog.models import BlogPost

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    password1 = forms.CharField(label="Set Password", widget=forms.PasswordInput(attrs={"placeholder":"Set your password","class":"form-control"}))
    password2 = forms.CharField(label="Confirm Password (again)", widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password","class":"form-control"}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"email":"Email"}
        widgets = {
            "username":forms.TextInput(attrs={"placeholder":"Enter username","class":"form-control"}),
            "first_name":forms.TextInput(attrs={"placeholder":"Enter first name","class":"form-control"}),
            "last_name":forms.TextInput(attrs={"placeholder":"Enter last name","class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter email","class":"form-control"}),
        }


# class LoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.label_suffix = ""

#     username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"placeholder":"Enter username","class":"form-control"}))
#     password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder":"Enter password","class":"form-control"}))
#     class Meta:
#         model = User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    username = UsernameField(label="Username", widget=forms.TextInput(attrs={"placeholder":"Enter username", "autofocus":True,"class":"form-control"}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={"placeholder":"Enter password", "autocolplete":"current-password","class":"form-control"}))
    class Meta:
        model = User


class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        
    class Meta:
        model = BlogPost
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter blog title", "class": "form-control"}),
            "description": forms.Textarea(attrs={"placeholder": "Enter blog description", "class": "form-control", "rows": 5, "cols": 50}),
        }
