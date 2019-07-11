import random

from binarytree import build
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BinaryTree
from .serializers import BinaryTreeSerializer


def create_tree():
    values = [random.randint(1, 20) for _ in range(20)]
    root = build(values)
    return root, ', '.join(str(e) for e in values)


class BinaryTreeViewSet(viewsets.ModelViewSet):
    queryset = BinaryTree.objects.all()
    serializer_class = BinaryTreeSerializer

    def create(self, request, *args, **kwargs):
        _, tree = create_tree()
        data = dict(request.data)
        if isinstance(data['name'], list):
            name = data['name'][0]
        data['name'] = name
        data['tree'] = tree
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.data, status=status.HTTP_400_BAD_REQUEST)
