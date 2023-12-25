from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def Home(request):
    return render(request,"home.html")

def signin(request):
    return render(request,"signin.html")

def logoutApi(request):
    logout(request)
    return redirect("/")

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


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Email: {email}, Password: {password}")

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            # return HttpResponse("Hai, Success!")
            return redirect("Home")
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials'})

    return HttpResponse("Invalid Request")
