from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from trips.models import Review

def landing(request):
    return render(request, "trips/index.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("overview")

        else:
            return render(
                request,
                "trips/login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "trips/login.html")


def forgot_password(request): 
    return render(request, "trips/forgot_password.html")


def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        password_confirm = request.POST["password_confirm"]

        if password != password_confirm:
            return render(request, "trips/signup.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "trips/signup.html", {"error": "This username is already taken."})

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        messages.success(
            request, 
            "Your account was successfully created."
        )
        return redirect("login")
    
    else:
        return render(request, "trips/signup.html")


@login_required
def overview(request):

    visited_count = Review.objects.filter(
        author=request.user
    ).count()
    visited_percentage = round(
        visited_count / 195 * 100, 1
    )

    context = {
        "visited_count": visited_count,
        "visited_percentage": visited_percentage,
    }
    
    return render(request, "trips/overview.html", context)

@login_required
def add_review(request):

    if request.method == "POST":
        country = request.POST["country"]

        # Check if the user has already reviewed this country
        if Review.objects.filter(author=request.user, country=country).exists():
            return render(request, "trips/add_review.html", {"error": "You have already reviewed this country."})

        Review.objects.create(
            country=country,
            overall_score=request.POST["overall_score"],
            comment=request.POST["comment"],
            author=request.user,
        )
        return redirect("overview")

    return render(request, "trips/add_review.html")

@login_required
def profile(request):
    return render(request, "trips/view_profile.html")

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.bio = request.POST["bio"]

        if "image" in request.FILES:
            profile.image = request.FILES["image"]

        profile.save()

        return redirect("profile")

    return render(request, "trips/edit_profile.html")

@login_required
def visited_countries(request):
    reviews = Review.objects.filter(author=request.user)
    context = {
        "reviews": reviews,
    }
    return render(request, "trips/visited_countries.html", context)

@login_required
def country_detail(request, review_id):
    review = get_object_or_404(
        Review,
        author=request.user,
        id=review_id
    )
    return render(request, "trips/country_detail.html", {
        "review": review,
    })


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        author=request.user,
    )

    if request.method == "POST":
        review.delete()
    return redirect("visited_countries")

def wishlist(request):
    return HttpResponse("Wishlist")


