from django_filters import rest_framework as filters
from .models import Post
class PostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='icontains')

    created_after = filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    created_before = filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['title','created_after', 'created_before']
