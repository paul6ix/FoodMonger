from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import model_food
from .forms import FoodForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
# def index(request):
#     food_list = model_food.objects.all()
#     context = {
#         'food_list': food_list
#
#     }
#     return render(request, 'Food/index.html', context)

# def food_detail(request, item_id):
#     detail = model_food.objects.get(pk=item_id)
#     context = {
#         'detail': detail,
#     }
#     return render(request, 'Food/food_detail.html', context)

# def add_food(request):
#     form = FoodForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     context = {
#         'form': form
#
#     }
#     return render(request, 'Food/add_food.html', context)


# implementing class based views in django
class ClassViewIndex(ListView):
    model = model_food
    template_name = 'Food/index.html'
    context_object_name = 'food_list'


class ClassFoodDetail(DetailView):
    model = model_food
    template_name = 'Food/food_detail.html'
    context_object_name = 'detail'


class ClassAddFood(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = model_food
    fields = ['food_name', 'food_desc', 'food_price', 'food_image']
    template_name = 'Food/add_food.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def edit_food(request, id):
    item = model_food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'Food/add_food.html', context)


def delete_food(request, id):
    item = model_food.objects.get(id=id)
    item.delete()

    context = {

        'item': item
    }
    return render(request, 'Food/delete_food.html', context)
