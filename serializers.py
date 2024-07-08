"""
Serializers for the app.
"""
from rest_framework import serializers
from .models import Restourant, Recipe, Ingredient, RestaurantIngredient, RecipeIngredient

class Restourant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Restourant
        fields = '__all__'

class Recipe_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class Ingredient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RestaurantIngredient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantIngredient
        fields = '__all__'

class RecipeIngredient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
