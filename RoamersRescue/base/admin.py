from django.contrib import admin
from .models import User, Review, Post, Topic


admin.site.register(User)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(Topic)

# Register your models here.
