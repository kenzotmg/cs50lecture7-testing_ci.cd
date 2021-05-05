from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Tweet(models.Model):
    content = models.CharField(max_length=140)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tweets")
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "content" : self.content,
            "author" : self.author,
            "timestamp" : self.timestamp
        }

class Likes(models.Model):
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE,related_name="likedTweet")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="liker")

class Follows(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followeds")
    followed = models.ForeignKey(User,on_delete=models.CASCADE,related_name="followers")