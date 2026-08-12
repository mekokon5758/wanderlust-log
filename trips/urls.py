from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

# path("login/", views.login_view, name="login")
# This means if the url is ~/login/, go check views.py -> def login_view

urlpatterns = [
    path("", views.landing, name="landing"),

    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),

    path(
        "forgot-password/",
        auth_views.PasswordResetView.as_view(
            template_name="trips/forgot_password.html"
        ),
        name="forgot_password",
    ),

    path(
        "forgot-password/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="trips/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="trips/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="trips/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("overview/", views.overview, name="overview"),

    path("add-review/", views.add_review, name="add_review"),

    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    path("visited/", views.visited_countries, name="visited_countries"),
    path("visited/<int:review_id>/", views.country_detail, name="country_detail"),

    path("visited/<int:review_id>/delete", views.delete_review, name="delete_review"),

    #path("wishlist/", views.wishlist, name="wishlist"),
]