"""
Views for the app.
"""
from rest_framework import generics
from .models import Restourant, Recipe, Ingredient, RestaurantIngredient, RecipeIngredient
from .serializers import Restourant_Serializer, Recipe_Serializer, Ingredient_Serializer, RestaurantIngredient_Serializer, RecipeIngredient_Serializer

class Restourant_view(generics.ListCreateAPIView):
    queryset = Restourant.objects.all()
    serializer_class = Restourant_Serializer

class Restourant_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restourant.objects.all()
    serializer_class = Restourant_Serializer

class Recipe_view(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipe_Serializer

class Recipe_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = Recipe_Serializer

class Ingredient_view(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = Ingredient_Serializer

class Ingredient_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = Ingredient_Serializer

class Recipes_by_ingredient(generics.ListAPIView):
    serializer_class = Recipe_Serializer

    def get_queryset(self):
        ingredient_name = self.kwargs.get('ingredient_name')
        return Recipe.objects.filter(recipeingredient__ingredient__ingredient_name=ingredient_name)

class Ingredients_by_recipe(generics.ListAPIView):
    serializer_class = Ingredient_Serializer

    def get_queryset(self):
        recipe_name = self.kwargs.get('recipe_name')
        return Ingredient.objects.filter(recipeingredient__recipe__recipe_name=recipe_name)

class Ingredients_by_restaurant(generics.ListAPIView):
    serializer_class = Ingredient_Serializer

    def get_queryset(self):
        restaurant_name = self.kwargs.get('restaurant_name')
        return Ingredient.objects.filter(restaurantingredient__restourant__resto_name=restaurant_name)

class Restaurants_by_recipe(generics.ListAPIView):
    serializer_class = Restourant_Serializer

    def get_queryset(self):
        recipe_name = self.kwargs.get('recipe_name')
        return Restourant.objects.filter(recipe__recipe_name=recipe_name)
