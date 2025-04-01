from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login  , logout
from django.contrib.auth.models import User
from blog.models import *

# Create your views here.

def home(request):
    allPosts = Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'home/home.html' , context)
    

def about(request):
    return render(request, 'home/about.html')
    

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, 'Please fill the form correctly.')
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Form has been submitted successfully.')
    return render(request, 'home/contact.html')


def search(request):
    query=request.GET['search']
    if query:
        if len(query)<50:
            allPostsTitle = Post.objects.filter(title__icontains=query)
            allPostsContent = Post.objects.filter(content__icontains=query)
            allPosts = allPostsTitle.union(allPostsContent)
            if allPosts:
                context = {'allPosts':allPosts , 'query': query}
                return render(request,'home/search.html',context)
            else:
                message = " Not Found "
                message2 = " Try Another Keywords "
                return render(request, 'home/search.html',{'message': message , 'message2': message2 ,'query': query})

        else:
            message = " Not Found "
            message2 = " Try Another Keywords "
            return render(request, 'home/search.html',{'message': message , 'message2': message2 , 'query': query})
    
    else:
        return render(request, 'home/home.html')
    

def handleSignup(request):
    if request.method=='POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #checks

        usernamecheck = User.objects.filter(username=username)
        if usernamecheck:
            messages.error(request, "User name already taken. Please try another user name!")
            return redirect('home')

        emailcheck = User.objects.filter(email=email)
        if emailcheck:
            messages.error(request, "This email has been already registered.")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "User name should be in numbers and letters")
            return redirect('home')
        if pass1 == pass2:
            myuser = User.objects.create_user(username , email , pass1)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('home')

        else:
            messages.error(request, "Password doesn't match.")
            return redirect('home')
    else:
        return HttpResponse(" 404 Not Found ")        
    

def handleLogin(request):
    if request.method == 'POST':
        loginuname = request.POST['loginuname']
        loginpassword = request.POST['loginpassword']

    user = authenticate(username = loginuname , password = loginpassword)

    if user:
        login(request , user)
        messages.success(request,"Successfully Logged In .")
        return redirect('home')

    else:
        messages.success(request,"Invalid Credentials. Please Try Again .")
        return redirect('home') 
    
    return HttpResponse("404 Not Found")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out .")
    return redirect('home')