from django.shortcuts import render
from django.http import HttpResponse
from .models import model_food
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
