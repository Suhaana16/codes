from django.shortcuts import render
from .models import Registation
# Create your views here
def home(request):
    return render(request, 'homepage.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Save the data to the database
        user = Registation(username=username, email=email, password=password)
        user.save()
    
    return render(request, 'register.html')