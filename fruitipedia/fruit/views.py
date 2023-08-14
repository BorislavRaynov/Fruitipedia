from django.shortcuts import render, redirect
from .models import Fruit
from .forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
# Create your views here.

# create_fruit, fruit_details, fruit_edit, fruit_delete

def create_fruit(request):
    form = CreateFruitForm()

    if request.method == 'POST':
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'fruitipedia/fruit/create-fruit.html', context=context)

def fruit_details(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()

    context = {
        'fruit': fruit
    }

    return render(request, 'fruitipedia/fruit/details-fruit.html', context=context)


def fruit_edit(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()
    form = EditFruitForm(instance=fruit)

    if request.method == 'POST':
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruitipedia/fruit/edit-fruit.html', context=context)

def fruit_delete(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()
    form = DeleteFruitForm(instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruitipedia/fruit/delete-fruit.html', context=context)
