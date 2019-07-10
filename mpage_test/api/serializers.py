from rest_framework.serializers import ModelSerializer

from .models import Movie


class MovieSerializer(ModelSerializer):
    """
    Movie Serializer
    """
    class Meta:
        model = Movie
        fields = "__all__"
