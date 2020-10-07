from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader


class Index(APIView):
    def get(self, request, format=None):
        template = loader.get_template('movielist/index.html')
        context = {
            'latest_question_list': True,
        }
        return HttpResponse(template.render(context, request))

