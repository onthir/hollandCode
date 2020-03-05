from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

#  method to register account
def register(request):

    # check if the user is already logged in
    if request.user.is_authenticated:
        return redirect("main:home")

    # if not logged in
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST or None)

            # check if the form is valid
            if form.is_valid():

                user = form.save(commit=False)
                user.is_active = True

                # check if the email already exists
                users = User.objects.all()

                duplicate = False
                for u in users:
                    if user.email == u.email:
                        error_message = "Email Already Exists"
                        duplicate = True
                        break
                if duplicate:
                    return render(request, 'accounts/register.html', {"error_message": "Email Already Exists", "form": form})       
                else:
                    user.save()
                return redirect("accounts:login_user")
        else:
            form = RegistrationForm(request.POST or None)
        return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            # now we get the data from html templates
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticating the credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is notNone") #meaning that the credentials are correct
                if user.is_active:
                    login(request, user)
                    return redirect("main:home")
                else:
                    return render(request, 'accounts/login.html', {'error-message': 'Your account has been banned.'})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Invalid Username or Password'})
        return render(request, 'accounts/login.html')

# logout user
# logout
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts:login_user")
    else:
        return redirect("accounts:login_user")
