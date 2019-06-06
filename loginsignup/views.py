from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from loginsignup.forms import SignUpForm
from student_info import settings
# Create your views here.


# def signup(request):
#     if request.method == "POST":
#         form =SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return render(request,"loginsignup/login.html")
#     else:
#         form =SignUpForm()
#         return render(request, "loginsignup/signup.html", {"form": form})



def mylogin(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user and user.is_staff is False:
            login(request,user)
            return redirect('homepage:index')
        elif user and user.is_staff is True:
            login(request,user)
            return redirect('detailabtstudent:dashboard')
        else:
            return redirect('loginsignup:login')
    return render(request, "loginsignup/login.html")

def mylogout(request):
    logout(request)
    return redirect("loginsignup:login")