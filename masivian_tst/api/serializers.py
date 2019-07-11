from rest_framework.serializers import ModelSerializer

from .models import BinaryTree


class BinaryTreeSerializer(ModelSerializer):
    """
    """
    class Meta:
        model = BinaryTree
        fields = '__all__'
