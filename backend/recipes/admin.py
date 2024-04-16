from django.contrib import admin
from django.contrib.admin import display

from .models import (Favorites, Ingredient, IngredientForRecipe, Recipe,
                     ShoppingCart, Tag)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'quantity_in_favorites')
    readonly_fields = ('quantity_in_favorites',)
    list_filter = ('author', 'name', 'tags',)
    empty_value_display = '-пусто-'

    @display(description='Добавлено в избранное')
    def quantity_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
    empty_value_display = '-пусто-'


@admin.register(Favorites)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
    empty_value_display = '-пусто-'


@admin.register(IngredientForRecipe)
class IngredientForRecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)
    empty_value_display = '-пусто-'
