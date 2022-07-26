import graphene
from graphene_django import DjangoObjectType

from .models import Establishment


print(":)")


class EstablishmentType(DjangoObjectType):
    class Meta:
        model = Establishment
        fields = (
            "id",
            "direction",
            "name",
            "rating",
            "description",
        )


class Query(graphene.ObjectType):
    all_establishment = graphene.List(EstablishmentType)

    def resolve_all_establishment(root, info):
        return Establishment.objects.all()


schema = graphene.Schema(query=Query)
