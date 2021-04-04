from django.urls import path,re_path
from . import views

urlpatterns = [
    # main home
    path('', views.index, name="index"),
    # food details
    path('<int:item_id>', views.food_detail, name="detail"),

    # add food item
    path('add/', views.add_food, name="add"),
    # edit food item
    path('edit/<int:id>', views.edit_food, name="edit"),

    # delete food item

    path('delete/<int:id>', views.delete_food, name="delete")
]
