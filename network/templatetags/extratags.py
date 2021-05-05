from django import template
from ..models import Tweet,Likes

register = template.Library()

@register.filter(name='getLikeCountFromTweet')
def getLikeCountFromTweet(tweet):
    return tweet.likedTweet.count()

@register.filter(name='serializeTweet')
def serializeTweet(tweet):
    pass