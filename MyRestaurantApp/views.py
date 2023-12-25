from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("hai")

def signin(request):
    return HttpResponse("Signin")

def logout(request):
    return HttpResponse("logout")

def signup(request):
    return HttpResponse("Signup")