from django.http import HttpResponse, Http404
from django.shortcuts import render

from colis.models import Coli


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>hello world </h1>")

def coli_detail_view(request, coli_id, *args, **kwargs):
    try:
        coli = Coli.objects.get(id=coli_id)
    except:
        raise Http404
    
    return HttpResponse(f"<h1>hello {coli_id} </h1>")