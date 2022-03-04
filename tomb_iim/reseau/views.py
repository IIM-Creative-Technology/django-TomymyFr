from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, response, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User
from .forms import SignUpUserForm, CreatePostsForm

from .models import Posts
from django.utils import timezone


# Create your views here.

def index(request):
    # get all users
    users = User.objects.all()
    posts = Posts.objects.all()
    posts = posts.order_by('-created_at')
    return render(request, 'reseau/index.html', {'posts': posts, 'users': users})

def create(request):
    # check if user is logged in, else redirect to login page
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reseau/login/')
    if request.method == 'POST':
        form = CreatePostsForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return HttpResponseRedirect('/reseau/')
    else:
        form = CreatePostsForm()
    return render(request, 'reseau/create.html', {'form': form})

def details_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'reseau/details_post.html', {'post': post})

def like_post(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/reseau/login/')
    else:
        post = get_object_or_404(Posts, pk=pk)
        # if user has liked the post, then unlike it
        if request.user in post.liked_by.all():
            post.liked_by.remove(request.user)
            post.like -= 1
            post.save()
            return HttpResponseRedirect('/reseau/')
        # else, like it
        else:
            post.like += 1
            post.liked_by.add(request.user)
            post.save()
            return HttpResponseRedirect('/reseau/#post_' + str(post.id))

def delete_post(request, pk):
    # if user request is created by user, then delete post
    if request.user.is_authenticated:
        post = get_object_or_404(Posts, pk=pk)
        if request.user == post.created_by:
            post.delete()
            return HttpResponseRedirect('/reseau/')
        else:
            return HttpResponse("You are not allowed to delete this post.")
    else:
        return HttpResponseRedirect('/reseau/login/')

def message(request):
    return render(request, 'reseau/message.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/reseau/')
    else:
        form = AuthenticationForm()
    return render(request, 'reseau/login.html')

def user_register(request):
    if request.method == 'POST':
        form = SignUpUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return HttpResponseRedirect('/reseau/')
    else:
        form = SignUpUserForm()
    return render(request, 'reseau/register.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/reseau/')