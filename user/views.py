from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm
from .models import User

def home(request):
    return render(request,'home.html')

def register_user(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request,email=email,password=password)
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    context={
        'form':form
    }
    return render(request,'register.html',context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('login')
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')