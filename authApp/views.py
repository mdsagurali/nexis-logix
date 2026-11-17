
# Django shortcuts
from django.shortcuts import render, redirect

# Django authentication functions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Login protection for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Safe redirect validation
from django.utils.http import url_has_allowed_host_and_scheme

# Forms
from .forms import (
    RegisterForm,
    LoginForm,
    UserUpdateForm,
    ProfileUpdateForm,
)


# User Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = User.objects.create_user(
                username=username,
                password=password
            )

            login(request, user)
            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


# User Login
def login_view(request):
    error_message = None

    next_url = request.GET.get("next", "")

    if request.method == "POST":
        form = LoginForm(request.POST)

        # Preserve next URL after form submission
        next_url = request.POST.get("next", "")

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

                # Validate redirect URL before redirecting
                if next_url and url_has_allowed_host_and_scheme(
                    url=next_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure(),
                ):
                    return redirect(next_url)

                return redirect("home")

            else:
                error_message = "Invalid credentials"

    else:
        form = LoginForm()

    context = {
        "form": form,
        "error": error_message,
        "next": next_url,
    }

    return render(
        request,
        "accounts/login.html",
        context
    )


# User Logout
@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

    return redirect("home")


# Home View (Inventory Dashboard)
@login_required
def home_view(request):
    return render(request, "invApp/home.html")


# Protected View (Class-Based View)
class ProtectedView(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request,
            "registration/protected.html"
        )


# User Profile
@login_required
def profile_view(request):

    if request.method == "POST":

        u_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect("profile")

    else:
        u_form = UserUpdateForm(
            instance=request.user
        )

        p_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(
        request,
        "accounts/profile.html",
        context
    )
