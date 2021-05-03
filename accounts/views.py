from .models import Profile
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    # tanggal = datetime.datetime
    context = {'pesan': 'Welcome to ePica',
               }
    return render(request, 'accounts/home.html', context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if request.POST.get('terms_of_use'):
            terms_of_use = True
        else:
            terms_of_use = False
        if form.is_valid():
            saved_form = form.save()
            Profile.objects.create(user=saved_form, terms_of_use=terms_of_use)
            return redirect('home')
    else:
        form = SignUpForm()

    context = {
        'pesan': "Signup",
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)


def datepicker(request):
    return render(request, 'accounts/datepicker.html')
