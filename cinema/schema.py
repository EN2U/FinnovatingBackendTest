import graphene
import cinema.apps.establishment.schema as EstablishmentSchema
import cinema.apps.movie.schema as MovieSchema


class GlobalQuery(EstablishmentSchema.Query, MovieSchema.Query):
    pass


class GlobalMutation(MovieSchema.Mutation):
    pass


schema = graphene.Schema(query=GlobalQuery, mutation=GlobalMutation)
