from django.shortcuts import render

def signup_view(request):
    return render(request, 'auth/signup.html')

def login_view(request):
    return render(request, 'auth/login.html')