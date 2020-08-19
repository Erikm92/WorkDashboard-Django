from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dashboard.forms import RegistrationForm, EditProfileForm, userlinksForm, userheaderForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import  PasswordChangeForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, Http404

from .models import userlinks, userheader


# Create your views here.
def dashboard(request):
    linktomain=userlinks.objects.filter(user=request.user)
    linktotitle=userheader.objects.filter(user=request.user)
    linktoheader_1=userheader.objects.filter(header_id="header_1",user=request.user)
    link1=linktoheader_1.all()
    linktoheader_2=userheader.objects.filter(header_id="header_2", user=request.user)
    link2=linktoheader_2.all()
    linktoheader_3=userheader.objects.filter(header_id="header_3",user=request.user)
    link3=linktoheader_3.all()
    linktoheader_4=userheader.objects.filter(header_id="header_4",user=request.user)
    link4=linktoheader_4.all()
    linktoheader_5=userheader.objects.filter(header_id="header_5",user=request.user)
    link5=linktoheader_5.all()
    linktoheader_6=userheader.objects.filter(header_id="header_6",user=request.user)
    link6=linktoheader_6.all()

    return render(request, 'Dashboard.html',{'linktomain':linktomain,'linktotitle':linktotitle,'link1':link1,
    'link2':link2,'link3':link3,'link4':link4,'link5':link5,'link6':link6})
#need to add user error for url

def addurl(request, table_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    if request.method == 'POST':
   #     form = userlinksForm(request.POST)
   #     if form.is_valid():
   #need to figure out the logic here for if form.is_valid();
   #security risk
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
        faviconurl="https://www.google.com/s2/favicons?domain="+mainfavicon
    #     
        addingurl = userlinks.objects.create(mainname=mainname, main=main, mainfavicon=faviconurl, table_id=table_id)
        addingurl.user=request.user
        addingurl.save();
            #instance=form.save()
         #   instance.user=request.user
          #  instance.save()
        return redirect("/Dashboard")
    
      #  context={
       #     'form': form,
       # }
        
    return render(request,'addurl.html')

def addheader(request, header_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        header_name = request.POST['header_name']
        header_id = header_id
       
        
        addingheader = userheader.objects.create(header_name=header_name, header_id=header_id)
        addingheader.user=request.user
        addingheader.save();
        return redirect("/Dashboard")
    
    return render(request,'addheader.html')
   
def transferlink(request, pk):
    
    pk=pk
    linktomain=userlinks.objects.all().filter(pk=pk)
    linktotitle=userheader.objects.all().filter(user=request.user)
    

    return render(request,'transferlink.html', {'linktotitle':linktotitle , 'linktomain':linktomain})


def transfersave(request, pk):
    post = get_object_or_404(userlinks, pk=pk, )
    header_id=request.Get('headerchange')
    if header_id == "header_2":
        table_new_id= "table_2"
        change_table_id=userlinks.objects.get(pk=pk)
        change_table_id.table_id=table_new_id
        change_table_id.save()

    return redirect("/Dashboard")


def editurl(request, pk):
    pk=pk
    linktomain=userlinks.objects.all().filter(pk=pk)

    return render(request, 'editurl.html',{'linktomain':linktomain})

def edittitle(request, pk):
    pk=pk
    linktotitle=userheader.objects.all().filter(pk=pk)

    return render(request, 'edittitle.html',{'linktotitle':linktotitle})
    

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



def edit_url(request, pk):
#look into why i am using mainfavicon request and change variable, don't lead to anything
    post = get_object_or_404(userlinks,pk=pk)
    
    if request.method == "POST":
        mainfavicon = request.POST['mainfavicon']
        form = userlinksForm(request.POST, instance=post)
        mainfaviconchange = userlinksForm("mainfavicon")
        
        
        
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

def edit_header(request, pk):
    post = get_object_or_404(userheader,pk=pk)

    if request.method == 'POST':
        header_name = request.POST['header_name']  
        form = userheaderForm(request.POST, instance=post)
        header_id = request.POST['header_id']
       
        
        if form.is_valid():
            form.save()
        return redirect("/Dashboard")
    else:
        form = userheaderForm(instance=post)
    context={
        'form': form,
        'post': post,
     
    }
    return render(request,'editheaders.html',context)
    

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
            return redirect('login')
            
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