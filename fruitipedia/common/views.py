from django.shortcuts import render
from fruitipedia.fruit.models import Fruit
# Create your views here.

def index(request):
    return render(request, 'fruitipedia/common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'fruitipedia/common/dashboard.html', context=context)
