from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class model_food(models.Model):
    def __str__(self):
        return self.food_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    food_name = models.CharField(max_length=200)
    food_desc = models.CharField(max_length=200)
    food_price = models.IntegerField()
    food_image = models.CharField(max_length=1000,
                                  default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg?compress=1&resize=400x300")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
