from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')


# User Register
def register(request):
    form = UserCreationForm()
    if request.method =="POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request,'User Registered Successfully...')

    return render(request, 'register.html', {'form':form})


