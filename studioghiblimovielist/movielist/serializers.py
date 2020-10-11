from movielist.models import Film, Person
from rest_framework import serializers


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            "name",
            "gender",
        )


class FilmSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(many=True)

    class Meta:
        model = Film
        fields = (
            "id",
            "title",
            "description",
            "director",
            "producer",
            "release_date",
            "rt_score",
            "people",
        )
