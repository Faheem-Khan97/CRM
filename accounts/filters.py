import django_filters
from django_filters import DateFilter


from .models import *

class OrderFilter(django_filters.FilterSet):
    startDate = DateFilter(field_name = 'dateCreated', lookup_expr = 'gte')
    endDate = DateFilter(field_name = 'dateCreated', lookup_expr = 'lte')
    class Meta:
        model = order
        fields = '__all__'

        exclude = ['customer','dateCreated']