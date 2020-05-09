#import the registerization tools and models
from django.contrib import admin
from .models import Post, Comment

#post registerization
admin.site.register(Post)
admin.site.register(Comment)
