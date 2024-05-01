from django.contrib import admin
from django.urls import path
from app_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('add_post/', views.add_blog_post, name="add_post"),
    path('update_post/<int:blog_id>/', views.update_blog_post, name="update_post"),
    path('delete_post/<int:blog_id>/', views.delete_blog_post, name="delete_post"),
]
