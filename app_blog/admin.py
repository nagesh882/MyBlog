from django.contrib import admin
from app_blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ["blog_id", "title", "description"]
    list_display_links = ["title"]