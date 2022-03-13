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
            'id',
            'model',
            'year',
            'price',
            'bike_type',
            'manufacturer',
        )

class Query(graphene.ObjectType):
    bikes = graphene.List(BikeType)
    bike = graphene.Field(BikeType,id=graphene.Int())

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Bike.objects.get(pk=id)

        return None
   
    def resolve_bikes(self, info, **kwargs):
        return Bike.objects.all()

schema = graphene.Schema(query=Query)