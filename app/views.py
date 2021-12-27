from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pyexpat.errors import messages

from .models import Climber, Post
from .forms import AddPost, AddClimber
import datetime


def home(request):
    return render(request, 'home.html')


def posts(request):
    post_ent = Post.objects.all()
    viewed_post = request.session.get('viewed_post', {})
    return render(request, 'posts.html', {'posts': post_ent, 'viewed_post': viewed_post})


def team(request):
    climbers = Climber.objects.all()
    return render(request, 'team.html', {'climbers': climbers})


def post(request, id):
    p = Post.objects.get(id=id)
    viewed_post = request.session.get('viewed_post', {})
    viewed_post[id] = id
    request.session['viewed_post'] = viewed_post
    return render(request, 'post.html', {'p': p})


def post_o(request):
    p = Post.objects.filter(post_type='o')
    if p:
        context = {'posts': p}
        return render(request, 'def_post.html', context=context)
    else:
        return render(request, 'home.html')


def add_post(request):
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post_ent = Post()
            post_ent.title = form.cleaned_data['title']
            post_ent.subtitle = form.cleaned_data['subtitle']
            post_ent.content = form.cleaned_data['content']
            post_ent.post_type = form.cleaned_data['post_type']
            post_ent.location = form.cleaned_data['location']
            post_ent.image = form.cleaned_data['image']

            post_ent.issues = datetime.datetime.now()
            post_ent.climber = Climber.objects.get(email=request.user.email)

            post_ent.save()
            return redirect('posts')
    else:
        form = AddPost()

    return render(request, "add_post.html", {'form': form})


def add_user(request):
    if request.method == "POST":
        form = AddClimber(request.POST)

        if form.is_valid():
            climber = Climber()
            climber.name = form.cleaned_data['name']
            climber.email = form.cleaned_data['email']
            climber.password = form.cleaned_data['email']

            user = form.save()
            login(request, user)
            return redirect('home/')
    else:
        form = AddClimber()

    return render(request, "new_user.html", {'form': form})


def posts_filter(request, post_type):
    p = Post.objects.filter(post_type=post_type)
    if p:
        context = {'posts_filter': p}
        return render(request, 'posts_filter.html', context=context)
    else:
        messages.error(request, "There are no post by this type")
        return render(request, 'posts.html')
