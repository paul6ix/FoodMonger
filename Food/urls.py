from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>', views.food_detail, name="detail"),
    path('home/', views.food_item, name="home")
]
