import graphene
from cinema.apps.establishment.schema import Query as EstablishmentQuery
from cinema.apps.movie.schema import Query as MovieQuery


class GlobalQuery(EstablishmentQuery, MovieQuery):
    pass


schema = graphene.Schema(query=GlobalQuery)
