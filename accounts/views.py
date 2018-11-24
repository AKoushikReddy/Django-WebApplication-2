from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeForm, ProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# Home view available for all users.
# returns home page.

# def home(request):
#     return render(request, "accounts/user_page.html", {"username": request.user, })

@login_required
def home(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, "accounts/user_page.html", {"user": request.user, 'profile': profile})


# Register View, redirects to the login view if Registration Form is valid , uses RegisterForm

def register_user(request):
    if request.method == "GET":
        f = RegisterForm()

    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/welcome")

    return render(request, "accounts/regs.html", {"form": f})


# Edit Account Information, uses ChangeForm, redirects to the home view if Registration Form is valid
@login_required
def edit_user(request):
    if request.method == "GET":
        f = ChangeForm(instance=request.user)

    if request.method == "POST":
        f = ChangeForm(request.POST, instance=request.user)
        if f.is_valid():
            f.save()
            return redirect("home")

    return render(request, "accounts/edit_info.html", {"form": f})


# Change Password view,uses PasswordChangeForm (imported from django)
#  Make sures that the user is logged in after changing the form
# With the help of update_session_auth_hash
# Redirect to home view , fi form is valid ( password changed)

@login_required
def change_pass(request):
    if request.method == "GET":
        f = PasswordChangeForm(user=request.user)

    if request.method == "POST":
        f = PasswordChangeForm(data=request.POST, user=request.user)
        if f.is_valid():
            f.save()
            # form.user is user not request.user, if request.user is used it takes anonymous user
            update_session_auth_hash(request, f.user)
            return redirect("home")

    return render(request, "accounts/change_pass.html", {"form": f})


# User Profile View

@login_required
def update_profile(request):
    # Profile is the UserProfile of respective User
    # Which is used as instance in form
    # objects.get Function used for any  relationship in databases
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "GET":
        f = ProfileForm(instance=profile)

    if request.method == "POST":
        f = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if f.is_valid():
            profile.user = request.user
            f.save()
            # form.user is user is not used here
            update_session_auth_hash(request, request.user)
            return redirect("home")

    return render(request, "accounts/profile.html", {"form": f})


