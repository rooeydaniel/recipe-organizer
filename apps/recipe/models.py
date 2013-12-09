from django.db import models
from apps.authentication.models import User


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        ordering = ('created',)


class RecipeList(models.Model):
    recipe_list_id = models.AutoField(primary_key=True)
    recipe_list_name = models.CharField(max_length=100)
    created = models.DateTimeField()

    class Meta:
        ordering = ('created',)


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    recipe_lists = models.ManyToManyField(RecipeList)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.CharField(max_length=4000)
    recipe_directions = models.CharField(max_length=4000)
    recipe_notes = models.CharField(max_length=4000)
    recipe_yield = models.CharField(max_length=20)
    recipe_prep_time = models.IntegerField()
    recipe_cook_time = models.IntegerField()
    recipe_total_time = models.IntegerField()
    recipe_source = models.CharField(max_length=255)
    private = models.IntegerField()
    archive = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        ordering = ('created',)


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe)
    measurement = models.IntegerField()
    measurement_type = models.CharField(max_length=10)

    class Meta:
        ordering = ('ingredient_name',)