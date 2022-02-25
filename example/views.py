from rest_framework.viewsets import ModelViewSet
from api.serializers import IndustrySerializer, CompanySerializer, PersonSerializer
from .models import Industry, Company, Person


class IndustryViewSet(ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
