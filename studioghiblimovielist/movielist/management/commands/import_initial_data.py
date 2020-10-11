from django.core.management.base import BaseCommand
from movielist.tasks import get_films_and_people

"""
Just in case celery goes up a bit late and the database needs to be filled with initial data 
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_films_and_people()
