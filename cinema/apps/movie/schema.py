import graphene
from graphene_django import DjangoObjectType

from .models import Movie
from cinema.apps.establishment.models import Establishment


class MovieInput(graphene.InputObjectType):
    title = graphene.String()
    category = graphene.String()
    director = graphene.String()
    premiere_date = graphene.Date()
    expiration_date = graphene.Date()
    duration = graphene.Int()
    cinema = graphene.ID()


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

    movie_by_title = graphene.List(
        MovieType, title=graphene.String(required=True)
    )

    movie_by_category = graphene.List(
        MovieType, category=graphene.String(required=True)
    )

    def resolve_all_movie(root, info):
        return Movie.objects.all()

    def resolve_movie_by_title(root, info, title):
        return Movie.objects.filter(title__icontains=title)


class CreateMovie(graphene.Mutation):
    class Arguments:
        movie_data = MovieInput(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_data=None):
        establishment_instance = Establishment.objects.get(
            pk=movie_data.cinema
        )

        movie_instance = Movie(
            title=movie_data.title,
            category=movie_data.category,
            director=movie_data.director,
            premiere_date=movie_data.premiere_date,
            expiration_date=movie_data.expiration_date,
            duration=movie_data.duration,
            cinema=establishment_instance,
        )

        movie_instance.save()
        return CreateMovie(movie=movie_instance)


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
