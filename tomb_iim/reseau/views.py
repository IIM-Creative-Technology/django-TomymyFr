from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, response, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import SignUpUserForm, CreatePostsForm

from .models import Posts
from django.utils import timezone


# Create your views here.

def index(request):
    posts = Posts.objects.all()
    posts = posts.order_by('created_at')
    return render(request, 'reseau/index.html', {'posts': posts})

def create(request):
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