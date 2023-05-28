from user.models import BotifyUser
import graphene
# from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class BotifyUserType(DjangoObjectType):
    class Meta:
        model = BotifyUser
        fields = "__all__"


class Query:
    all_users = graphene.List(BotifyUserType)

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return BotifyUser.objects.all()
