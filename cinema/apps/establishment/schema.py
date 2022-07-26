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

    establishment_by_name = graphene.List(
        EstablishmentType, name=graphene.String(required=True)
    )

    establishment_by_direction = graphene.List(
        EstablishmentType, name=graphene.String(required=True)
    )

    def resolve_all_establishment(root, info):
        return Establishment.objects.all()

    def resolve_establishment_by_name(root, info, name):
        return Establishment.objects.filter(name__icontains=name)

    def resolve_establishment_by_direction(root, info, direction):
        return Establishment.objects.filter(direction__icontains=direction)


schema = graphene.Schema(query=Query)
