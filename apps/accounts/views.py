from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
# Create your views here.

def registerView(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request,'register.html',{'form':form})
