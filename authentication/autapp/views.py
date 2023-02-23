from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth 
# Create your views here.

def home(request):
    
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            messages.error(request,'Both password are not same')
            return redirect('register')
        elif User.objects.filter(username = username).exists():
            messages.error(request,'name is used')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.error(request,'email is used')
            return redirect('register')
        else:
            userdata = User.objects.create_user(username = username,first_name= firstname,last_name=lastname,email = email,password=password1)
            userdata.save()
            return redirect('login')
    return render(request,'reg/reg.html',)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)
       
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    
    return render(request,'reg/login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')