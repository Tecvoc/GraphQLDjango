from cookbook.ingredients.models import Category, Ingredient
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
import graphene


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        # interfaces = (Node, )
        # filter_fields = ['name', 'ingredients']


class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        # interfaces = (Node, )
        # filter_fields = {
        #     'name': ['exact', 'icontains', 'istartswith'],
        #     'notes': ['exact', 'icontains'],
        #     'category': ['exact'],
        #     'category__name': ['exact'],
        # }


# class Query(object):
#     category = Node.Field(CategoryNode)
#     all_categories = DjangoFilterConnectionField(CategoryNode)
#
#     ingredient = Node.Field(IngredientNode)
#     all_ingredients = DjangoFilterConnectionField(IngredientNode)


class Query(object):
    all_categories = graphene.List(CategoryNode)
    all_ingredients = graphene.List(IngredientNode)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()
