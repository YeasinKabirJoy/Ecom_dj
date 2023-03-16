from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.views import View
from .forms import RegistrationForm
from .models import User

# def home(request):
#     return render(request,'home.html')

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegisterUser(View):
    def get(self,request):
        form = RegistrationForm()
        context={
        'form':form
        }
        return render(request,'register.html',context)

    def post(self,request):
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

# def register_user(request):
#     form = RegistrationForm()

#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(request,email=email,password=password)
#             login(request,user)
#             return redirect(request.GET['next'] if 'next' in request.GET else 'home')
#     context={
#         'form':form
#     }
#     return render(request,'register.html',context)

class LoginUser(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'login.html')
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('login')
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        return render(request,'login.html')
    


# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == "POST":
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return redirect('login')
    #     user = authenticate(request,email=email,password=password)

    #     if user is not None:
    #         login(request,user)
    #         return redirect(request.GET['next'] if 'next' in request.GET else 'home')
    # return render(request,'login.html')

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')
# def logout_user(request):
#     logout(request)
#     return redirect('login')