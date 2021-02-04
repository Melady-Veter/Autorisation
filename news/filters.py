from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {'headline': ['icontains'],
                  'create_time': ['range'],
                  'author': ['exact'],
                  }