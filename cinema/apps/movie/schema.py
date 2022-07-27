import graphene
from graphene_django import DjangoObjectType

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


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


class MovieKeysInput(graphene.InputObjectType):
    title = graphene.String()
    category = graphene.String()
    director = graphene.String()


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
        try:
            establishment_instance = Establishment.objects.get(
                pk=movie_data.cinema
            )
        except ObjectDoesNotExist:
            raise Exception("The cinema does not have this film")

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


class UpdateMovie(graphene.Mutation):
    class Arguments:
        movie_data = MovieInput(required=True)
        movie_keys = MovieKeysInput(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, movie_data=None, movie_keys=None):
        movie_instance = Movie.objects.get(
            title=movie_keys.title,
            director=movie_keys.director,
            category=movie_keys.category,
        )

        if movie_data:
            for key, value in movie_data.items():
                if key == "cinema":
                    try:
                        value = Establishment.objects.get(pk=movie_data.cinema)
                    except ObjectDoesNotExist:
                        raise Exception("The cinema does not have this film")
                setattr(movie_instance, key, value)

            movie_instance.save()
            return UpdateMovie(movie=movie_instance)
        return UpdateMovie(movie=None)


class DeleteMovie(graphene.Mutation):
    class Arguments:
        movie_keys = MovieKeysInput(required=True)

    movie = graphene.Field(MovieType)

    def mutate(root, info, movie_keys):
        movie_instance = Movie.objects.get(
            title=movie_keys.title,
            director=movie_keys.director,
            category=movie_keys.category,
        )
        movie_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()
