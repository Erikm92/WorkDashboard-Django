from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import  PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from . models import userlinks


# Create your views here.
def dashboard(request):
    
    linktomain=userlinks.objects.all()
    return render(request, 'Dashboard.html',{'linktomain':linktomain})

def addurl(request):
    if request.method == 'POST':
        mainname = request.POST['mainname']
        main = request.POST['main']
        mainfavicon = ""
        counter=0
        total_letters=0
        charc=[]
   
        for i in main:
        
            charc += [i]
        for x in charc:
            total_letters += 1
            if x=='/':
                counter +=1
                if counter == 3:
                    for x in range(total_letters):
                        mainfavicon += charc[x]
                
        
        addingurl = userlinks.objects.create(mainname=mainname, main=main, mainfavicon=mainfavicon)
        addingurl.save();
        return redirect("/Dashboard")
    else:
        return render(request,'addurl.html')
   
# need to add an extra column to table to favicon due to the foor loop that loads them all
   
def editurl(request):

    linktomain=userlinks.objects.all()

    return render(request, 'editurl.html',{'linktomain':linktomain})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/Dashboard")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'Signin.html')

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Dashboard')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'register.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/Dashboard/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'editprofile.html', args)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST or None, user = request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/Dashboard/profile')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'forms': form}
        return render(request, 'changepassword.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/Dashboard/login')
    #need to be changes to homepage (Welcome to Dashboard etc)

def dialog(request):
    

    return render(request, 'dialog.html')