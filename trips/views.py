from django.contrib import messages
from django.shortcuts import redirect, render
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
        password_confirm = request.POST["password_confirm"]

        if password != password_confirm:
            return render(request, "trips/signup.html", {
                "error": "Passwords do not match"
            })

        user = User.objects.create_user(
            username=username,
            password=password
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
        Review.objects.create(
            country=request.POST["country"],
            overall_score=request.POST["overall_score"],
            comment=request.POST["comment"],
            author=request.user,
        )
        return redirect("overview")

    return render(request, "trips/add_review.html")

@login_required
def profile(request):
    return HttpResponse("Profile")

@login_required
def edit_profile(request):
    return HttpResponse("Edit Profile")

@login_required
def visited_countries(request):
    return HttpResponse("Visited Countries")

@login_required
def country_detail(request, country):
    return HttpResponse(f"Country: {country}")


def wishlist(request):
    return HttpResponse("Wishlist")


