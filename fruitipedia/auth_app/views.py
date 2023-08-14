from django.shortcuts import render, redirect
from fruitipedia.fruit.models import Fruit
from .models import Profile
from .forms import CreateProfileForm, EditProfileForm
# Create your views here.

def create_profile(request):
    form = CreateProfileForm()

    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form
    }

    return render(request, 'fruitipedia/auth_app/create-profile.html', context=context)

def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'fruitipedia/auth_app/edit-profile.html', context=context)

def details_profile(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'fruits': Fruit.objects.all()
    }

    return render(request, 'fruitipedia/auth_app/details-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()
    fruits = Fruit.objects.all()
    if request.method == 'POST':
        fruits.delete()
        profile.delete()
        return redirect('home-page')

    return render(request, 'fruitipedia/auth_app/delete-profile.html')
