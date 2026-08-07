from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

# path("login/", views.login_view, name="login")
# This means if the url is ~/login/, go check views.py -> def login_view

urlpatterns = [
    path("", views.landing, name="landing"),

    path("login/", views.login_view, name="login"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("signup/", views.signup, name="signup"),

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