from django.http import HttpResponse
from django.template import loader
from rest_framework.generics import ListAPIView

from movielist.models import Film
from movielist.serializers import FilmSerializer
import random


class Index(ListAPIView):
    queryset = Film.objects.all().order_by("-release_date")
    serializer_class = FilmSerializer

    def get(self, request):
        print("aaaaa")
        print("hello")
        print(random.random())
        template = loader.get_template("movielist/index.html")
        context = {
            "films": self.list(request).data,
        }
        return HttpResponse(template.render(context, request))
