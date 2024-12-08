from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm


def homepage(request):
    return render(request, 'accounts/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


# Function to handle login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Redirect to a dashboard or home page
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/login.html')


# Function to handle logout 
def logout_view(request):
    logout(request)
    return redirect('login')    