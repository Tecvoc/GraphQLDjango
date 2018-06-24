import cookbook.ingredients.schema
# import cookbook.recipes.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(cookbook.ingredients.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
