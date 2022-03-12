import graphene
from graphene_django import DjangoObjectType
from .models import Manufacturer, BikeType, Bike

class ManufacturerType(DjangoObjectType):
    class Meta:
        model = Manufacturer
        fields = (
            'name',
        )


class BikeTypeType(DjangoObjectType):
    class Meta:
        model = BikeType
        fields = (
            'name',
        )

class BikeType(DjangoObjectType):
    class Meta:
        model = Bike
        fields = (
            'model',
            'year',
            'price',
            'bike_type',
            'manufacturer',
        )

class Query(graphene.ObjectType):

    all_bikes = graphene.List(BikeType)

    def resolve_all_bikes(root,info):
        return Bike.objects.all()

schema = graphene.Schema(query=Query)