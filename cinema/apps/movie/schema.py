import graphene
from graphene_django import DjangoObjectType

from .models import Movie


class MovieType(DjangoObjectType):
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


class Query(graphene.ObjectType):
    all_movie = graphene.List(MovieType)

    establishment_by_title = graphene.List(
        MovieType, title=graphene.String(required=True)
    )

    establishment_by_category = graphene.List(
        MovieType, category=graphene.String(required=True)
    )

    def resolve_all_movie(root, info):
        return Movie.objects.all()

    def resolve_movie_by_title(root, info, title):
        return Movie.objects.filter(title__icontains=title)


schema = graphene.Schema(query=Query)
