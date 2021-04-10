from django.urls import path,re_path
from . import views

urlpatterns = [
    # main home
    path('', views.ClassViewIndex.as_view(), name="index"),
    # food details
    path('<int:pk>', views.ClassFoodDetail.as_view(), name="detail"),

    # add food item
    path('add/', views.ClassAddFood.as_view(), name="add"),
    # edit food item
    path('edit/<int:id>', views.edit_food, name="edit"),

    # delete food item

    path('delete/<int:id>', views.delete_food, name="delete")
]
