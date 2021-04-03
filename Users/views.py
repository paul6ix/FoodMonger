from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from .forms import RegisterForm


# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account was successfully created')
            return redirect('index')
    else:
        form = UserCreationForm()
        context = {
                'form': form
            }
        return render(request, 'Users/register.html', context)
