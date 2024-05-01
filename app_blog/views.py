from django.shortcuts import render, HttpResponseRedirect, redirect
from app_blog.forms import SignUpForm, LoginForm, BlogPostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from app_blog.models import BlogPost
from django.contrib.auth.models import Group

def home(request):
    blog_post = BlogPost.objects.all()
    context = {
        "posts":blog_post
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


from django.contrib.auth.models import Group

def dashboard(request):
    if request.user.is_authenticated:
        blog_posts = BlogPost.objects.all()
        user = request.user
        full_name = user.get_full_name()
        
        # Getting the groups of the logged-in user
        user_groups = user.groups.values_list('name', flat=True)
        
        # Filter groups to get only 'Editer' and 'Admin'
        relevant_groups = ['Editer', 'Admin']
        user_group_name = next((group for group in user_groups if group in relevant_groups), None)
        
        return render(request, "dashboard.html", {"posts": blog_posts, "full_name": full_name, "groups": user_group_name})
    else:
        return redirect("login")


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            groups = Group.objects.get(name="Editer")
            user.groups.add(groups)
            messages.success(request, "User become an editer!!!")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form":form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User logged in successfully!!!")
                    return redirect("dashboard")
        else:
            form = LoginForm()
        return render(request, "login.html", {"form":form})
    else:
        return redirect("dashboard")

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "User logged out successfully!!!")
        return redirect("login")
    else:
        return redirect("login")
    

def add_blog_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog_post = BlogPostForm(request.POST)
            if blog_post.is_valid():
                post_title = blog_post.cleaned_data["title"]
                post_desc = blog_post.cleaned_data["description"]

                blog_post_data = BlogPost(title=post_title, description=post_desc)
                blog_post_data.save()
                messages.success(request, "Post added successfully!!!")

                blog_post = BlogPostForm()
        else:
            blog_post = BlogPostForm()
        return render(request, "add_blog_post.html", {"posts":blog_post})
    else:
        return redirect("login")


def update_blog_post(request, blog_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog_post_id = BlogPost.objects.get(pk=blog_id)
            blog_post = BlogPostForm(request.POST, instance=blog_post_id)
            if blog_post.is_valid():
                blog_post.save()
                messages.success(request, "Post updated successfully!!!")
        else:
            blog_post_id = BlogPost.objects.get(pk=blog_id)
            blog_post = BlogPostForm(instance=blog_post_id)
        return render(request, "update_blog_post.html", {"posts":blog_post})
    else:
        return redirect("login")


def delete_blog_post(request, blog_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            blog_post_id = BlogPost.objects.get(pk=blog_id)
            blog_post_id.delete()
            return redirect("dashboard")
    else:
        return redirect("login")