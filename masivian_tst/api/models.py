from django.db import models


class BinaryTree(models.Model):
    name = models.CharField(max_length=50)
    root = models.CharField(max_length=50)

    def __str__(self):
        return self.name
