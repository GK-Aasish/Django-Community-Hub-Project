from django.shortcuts import render

def user_settings(request):
    return render(request, 'components/user_settings.html')