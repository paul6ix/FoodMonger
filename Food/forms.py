from django import forms
from .models import model_food


class FoodForm(forms.ModelForm):
    class Meta:
        model = model_food
        fields = ['food_name', 'food_desc', 'food_price', 'food_image']
