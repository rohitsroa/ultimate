import django_tables2 as tables
from .models import QueryInfo

class QueryInfoTable(tables.Table):
    class Meta:
        model = QueryInfo