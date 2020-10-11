from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, null=True)


class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.IntegerField()
    rt_score = models.IntegerField()
    people = models.ManyToManyField(Person, related_name="films",)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(unique=True, null=True)
