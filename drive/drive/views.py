from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')  # Cela doit être correct
    
def login_view(request):
    return render(request, 'login.html')

def signin_view(request):
    return render(request, 'signin.html')
