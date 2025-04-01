from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/blogHome.html',context)
    

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request,'blog/blogPost.html', context)




def postContent(request):
    if request.method == 'POST':
        postTitle = request.POST['postTitle']
        postAuthor = request.POST['postAuthor']
        postContent = request.POST['postContent']
        

        if postTitle and postAuthor and postContent:
            postSlug = '+'.join(postTitle.split(" "))
            yourPost = Post(title=postTitle , author=postAuthor, content=postContent, slug=postSlug)
            yourPost.save()
            messages.success(request, "Blog Successfully Saved.")
            

        else:
            messages.error(request, "Please Write Your Blog")
            

    return render(request, 'blog/postContent.html')
    
    