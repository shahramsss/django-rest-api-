from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    age = models.SmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
