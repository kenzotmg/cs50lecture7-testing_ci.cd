from django.contrib import admin
from .models import User,Tweet,Likes,Follows

class TweetAdmin(admin.ModelAdmin):
    list_display = ("content","author","timestamp")

class LikesAdmin(admin.ModelAdmin):
    list_display = ("tweet", "user")

class FollowsAdmin(admin.ModelAdmin):
    list_display = ("follower", "followed")
# Register your models here.
admin.site.register(User)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Likes, LikesAdmin)
admin.site.register(Follows, FollowsAdmin)