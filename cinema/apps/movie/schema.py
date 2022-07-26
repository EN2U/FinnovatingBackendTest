import graphene
from graphene_django import DjangoObjectType

from .models import Movie


class EstablishmentType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = (
            "title",
            "category",
            "director",
            "premiere_date",
            "expiration_date",
            "duration",
            "cinema",
        )
