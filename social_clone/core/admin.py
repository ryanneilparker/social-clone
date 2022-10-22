from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Admin model registrations.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)