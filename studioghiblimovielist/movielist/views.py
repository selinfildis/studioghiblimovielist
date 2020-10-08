import random

from django.http import HttpResponse
from django.template import loader
from django.views import View

from .helpers import get_films_and_people


class Index(View):
    def get(self, request):
        template = loader.get_template("movielist/index.html")
        context = {
            "films": get_films_and_people(),
            # 'refresh': random.random() For testing purposes
        }
        return HttpResponse(template.render(context, request))
