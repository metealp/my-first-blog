#import the registerization tools and models
from django.contrib import admin
from .models import Post

#post registerization
admin.site.register(Post)