from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("hai")

def signin(request):
    return render(request,"signin.html")

def logout(request):
    return HttpResponse("logout")

def signup(request):
    # return HttpResponse("Signup")
    return render(request,"signup.html")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

from .models import UserProfile
# from .serializers import UserProfileSerializer  # You need to create this serializer

@csrf_exempt
def signupApi(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')

        user = UserProfile.objects.create_user(email=email, password=password, name=name, age=age)
        return render(request,"signin.html",{"message": "User created successfully"})

    return JsonResponse({"message": "GET request received. Use POST for user registration."})
