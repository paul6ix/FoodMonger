from django.db import models


# Create your models here.

class model_food(models.Model):
    def __str__(self):
        return self.food_name

    food_name = models.CharField(max_length=200)
    food_desc = models.CharField(max_length=200)
    food_price = models.IntegerField()
    food_image = models.CharField(max_length=1000, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg?compress=1&resize=400x300")
