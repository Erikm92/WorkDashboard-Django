from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.forms import RegistrationForm, EditProfileForm, userlinksForm, userheaderForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import  PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404

from . models import userlinks, userheader


# Create your views here.
def dashboard(request):
    
    linktomain=userlinks.objects.all()
    linktoheader=userheader.objects.all()
    return render(request, 'Dashboard.html',{'linktomain':linktomain,'linktoheader':linktoheader})
#need to add user error for url
def addurl(request, table_id):
    if request.method == 'POST':
        mainname = request.POST['mainname']
        main = request.POST['main']
        mainfavicon = ""
        table_id= table_id
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
                
        
        addingurl = userlinks.objects.create(mainname=mainname, main=main, mainfavicon=mainfavicon, table_id=table_id)
        addingurl.save();
        return redirect("/Dashboard")
    else:
        return render(request,'addurl.html')
   

   
def editurl(request):

    linktomain=userlinks.objects.all()

    return render(request, 'editurl.html',{'linktomain':linktomain})

def edittitle(request):
    
    linktotitle=userheader.objects.all()

    return render(request, 'edittitle.html',{'linktotitle':linktotitle})

def new_title(request):
    form = userheaderForm(request.POST or None)

    if form.is_valid():
        form.save()
        
    else:
        form = userheaderForm()
    context={
        'form': form,
    }
    return render(request,'edittitle.html',context)
    

def edit_title(request, pk):
    post = get_object_or_404(userheader,pk=pk)

    if request.method == "POST":
        form = userheaderForm(request.POST, instance=post)

       
        if form.is_valid():
            form.save()
            return redirect("/Dashboard")
    else:
        form = userheaderForm(instance=post)
    context={
        'form': form,
        'post': post,
    }
    return render(request,'edittitleform.html', context)

def new_post(request):
    form = userlinksForm(request.POST or None)

    if form.is_valid():
        form.save()
        
    else:
        form = userlinksForm()
    context={
        'form': form,
    }
    return render(request,'editlink.html',context)

def edit_url(request, pk):
    post = get_object_or_404(userlinks,pk=pk)

    if request.method == "POST":
        form = userlinksForm(request.POST, instance=post)

       
        if form.is_valid():
            form.save()
            return redirect("/Dashboard")
    else:
        form = userlinksForm(instance=post)
    context={
        'form': form,
        'post': post,
    }
    return render(request,'editlink.html', context)


def delete_url(request, pk):
    post = get_object_or_404(userlinks, pk=pk)

    if request.method == "POST":
        form = userlinksForm(request.POST, instance=post)
        post.delete()
        return redirect("/Dashboard")
    else:
        form = userlinksForm(instance=post)
    context={
        'form': form,
        'post': post,
    }
    return render(request,'editlink.html', context)

def edit_header(request, header_id):
    if request.method == 'POST':
        header_name = request.POST['header_name']
        header_id = header_id
        
        addingheader = userheader.objects.create(header_name=header_name, header_id=header_id)
        addingheader.save();
        return redirect("/Dashboard")
    else:
        return render(request,'editheaders.html')
    

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