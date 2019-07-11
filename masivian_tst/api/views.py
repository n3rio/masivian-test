from rest_framework import viewsets

from .models import BinaryTree
from .serializers import BinaryTreeSerializer

# Create your views here.


class BinaryTreeViewSet(viewsets.ModelViewSet):
    queryset = BinaryTree.objects.all()
    serializer_class = BinaryTreeSerializer
