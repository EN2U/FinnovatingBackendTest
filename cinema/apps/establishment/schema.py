import graphene
from graphene_django import DjangoObjectType

from .models import Establishment


class EstablishmentInput(graphene.InputObjectType):
    id = graphene.ID()
    direction = graphene.String()
    name = graphene.String()
    rating = graphene.Int()
    description = graphene.String()


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


class CreateEstablishment(graphene.Mutation):
    class Arguments:
        establishment_data = EstablishmentInput(required=True)

    establishment = graphene.Field(EstablishmentType)

    def mutate(self, info, establishment_data=None):
        establishment_instance = Establishment(
            name=establishment_data.name,
            rating=establishment_data.rating,
            description=establishment_data.description,
            direction=establishment_data.direction,
        )

        establishment_instance.save()
        return CreateEstablishment(establishment=establishment_instance)


class UpdateEstablishment(graphene.Mutation):
    class Arguments:
        establishment_data = EstablishmentInput(required=True)

    establishment = graphene.Field(EstablishmentType)

    def mutate(self, info, establishment_data=None):
        establishment_instance = Establishment.objects.get(
            pk=establishment_data.id
        )

        if establishment_data:

            for key, value in establishment_data.items():
                setattr(establishment_instance, key, value)

            establishment_instance.save()
            return UpdateEstablishment(establishment=establishment_instance)
        return UpdateEstablishment(establishment=None)


class DeleteEstablishment(graphene.Mutation):
    class Arguments:
        establishment_id = graphene.ID()

    establishment = graphene.Field(EstablishmentType)

    def mutate(root, info, establishment_id):
        establishment_instance = Establishment.objects.get(pk=establishment_id)
        establishment_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_establishment = CreateEstablishment.Field()
    update_establishment = UpdateEstablishment.Field()
    delete_establishment = DeleteEstablishment.Field()
