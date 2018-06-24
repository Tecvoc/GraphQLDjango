from django.contrib import admin
from cookbook.ingredients.models import *

# Register your models here.

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_editable = ('name', 'category')


admin.site.register(Category)
