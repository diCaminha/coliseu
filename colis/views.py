from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from colis.models import Coli


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>hello world </h1>")

def coli_detail_view(request, coli_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JS or Java
    """
    status = 200
    data = {
        "id": coli_id,
    }
    try:
        coli = Coli.objects.get(id=coli_id)
        data['content'] = coli.content
    except:
        data['content'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)