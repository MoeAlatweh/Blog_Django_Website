from django.contrib import admin
# import post from model file
from .models import Post

# Register your models here.

# Register post models
admin.site.register(Post)