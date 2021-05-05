from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User,Tweet


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def postTweet(request):
    if request.method == "GET":
        return HttpResponseRedirect(reverse("index"))
    elif request.method == "POST":
        tweetContent = request.POST['tweet']
        author = request.user

        try:
            tweet = Tweet(content=tweetContent,author=author)
            tweet.save()
        except Exception as e:
            print(f"ERROR: {e}")

        return HttpResponseRedirect(reverse("index"))

@login_required(login_url='/login')
def allTweets(request):
    if request.method == 'GET':
        tweets = ''
        try:
            tweets = Tweet.objects.all()
        except Exception as e:
            print(f"ERROR: {e}")
            return render(request,"network/index.html")
        if tweets:
            tweets = tweets.order_by("-timestamp").all()
            return render(request,"network/alltweets.html", {
                "tweets" : tweets
            })
        else:
            return render(request,"network/alltweets.html")
