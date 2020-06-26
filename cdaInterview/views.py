from django.shortcuts import render
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect
# Create your views here.
from django import forms
from django.forms import ModelForm,Textarea,TextInput


class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]
        widgets = {
        'password': forms.PasswordInput(),
        }

def loginView(request):
    data = {}

    if request.method=="POST":
        username = request.POST.get('username')
        pwd = make_password(request.POST.get('password'))
        formsPost = loginForm(request.POST)

        queryset = User.objects.get(username=username)
        bool_login = request.POST.get('password')==queryset.password
        print(pwd, username, bool_login)
        if bool_login:
            
            return HttpResponseRedirect('/main/')

    forms = loginForm()
    data['forms']=forms

    return render(request, 'cdaInterview/login.html',{'form':forms})

def main(request):
    return render(request,'cdaInterview/main.html', {})

def contactUs(request):
    return render(request,'cdaInterview/contactus.html', {})