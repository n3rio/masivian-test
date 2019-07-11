from django.db import models


class BinaryTree(models.Model):
    name = models.CharField(max_length=50)
    tree = models.CharField(max_length=200)

    def __str__(self):
        return self.name
