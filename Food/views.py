from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import model_food
from .forms import FoodForm
from django.template import loader


# Create your views here.
def index(request):
    food_list = model_food.objects.all()
    context = {
        'food_list': food_list

    }
    return render(request, 'Food/index.html', context)


def food_item(request):
    return HttpResponse("This is the homepage")


def food_detail(request, item_id):
    detail = model_food.objects.get(pk=item_id)
    context = {
        'detail': detail,
    }
    return render(request, 'Food/food_detail.html', context)


def add_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form

    }
    return render(request, 'Food/add_food.html', context)
