"""
Models for the app.
"""
from django.db import models

class Restourant(models.Model):
    # Primary key for the restaurant
    resto_id = models.AutoField(primary_key=True)
    # Name of the restaurant
    resto_name = models.CharField(max_length=255)

    def __str__(self):
        return self.resto_name

class Recipe(models.Model):
    # Primary key for the recipe
    recipe_id = models.AutoField(primary_key=True)
    # Name of the recipe
    recipe_name = models.CharField(max_length=255)
    # Foreign key to the restaurant
    restourant = models.ForeignKey(Restourant, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    # Primary key for the ingredient
    ing_id = models.AutoField(primary_key=True)
    # Name of the ingredient
    ingredient_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ingredient_name

class RestaurantIngredient(models.Model):
    # Foreign key to the restaurant
    restourant = models.ForeignKey(Restourant, on_delete=models.CASCADE)
    # Foreign key to the ingredient
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class RecipeIngredient(models.Model):
    # Foreign key to the recipe
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Foreign key to the ingredient
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
