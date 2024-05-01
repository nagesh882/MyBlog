from django.db import models


class BlogPost(models.Model):
    blog_id = models.BigAutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()