import graphene

from user.apis.graphql import schema as user_schema

from graphene_django.debug import DjangoDebug


class Query(user_schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, auto_camelcase=False,)
