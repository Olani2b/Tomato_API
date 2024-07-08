"""
URL configuration for the app.
"""
from django.urls import path
from .views import (
    Restourant_view, Restourant_detail_view, Recipe_view, Recipe_detail_view,
    Ingredient_view, Ingredient_detail_view, Recipes_by_ingredient, 
    Ingredients_by_recipe, Ingredients_by_restaurant, Restaurants_by_recipe
)

urlpatterns = [
    path('restaurants/', Restourant_view.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', Restourant_detail_view.as_view(), name='restaurant-detail'),
    path('recipes/', Recipe_view.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', Recipe_detail_view.as_view(), name='recipe-detail'),
    path('ingredients/', Ingredient_view.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', Ingredient_detail_view.as_view(), name='ingredient-detail'),
    path('recipes/by_ingredient/<str:ingredient_name>/', Recipes_by_ingredient.as_view(), name='recipes-by-ingredient'),
]
urlpatterns = [
    path('recipes/by_ingredient/<str:ingredient_name>/', Recipes_by_ingredient.as_view(), name='recipes-by-ingredient'),
    path('ingredients/by_recipe/<str:recipe_name>/', Ingredients_by_recipe.as_view(), name='ingredients-by-recipe'),
    path('ingredients/by_restaurant/<str:restaurant_name>/', Ingredients_by_restaurant.as_view(), name='ingredients-by-restaurant'),
    path('restaurants/by_recipe/<str:recipe_name>/', Restaurants_by_recipe.as_view(), name='restaurants-by-recipe'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tomato_API.urls')),
]
