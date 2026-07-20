from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
    return render(request, "trips/overview.html")


def profile(request):
    return HttpResponse("Profile")


def edit_profile(request):
    return HttpResponse("Edit Profile")


def country_list(request):
    return HttpResponse("Visited Countries")


def country_detail(request, country):
    return HttpResponse(f"Country: {country}")


def wishlist(request):
    return HttpResponse("Wishlist")


