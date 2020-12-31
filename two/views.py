from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse

from .models import Ask

# Create your views here.
def root(request):

    return HttpResponse("hi hi")

def recent(request):
    # hard to implement with get_list_or_404
    # no function is_recent() is allowed as a parameter
    pass


def filter(request):

    query = get_list_or_404(Ask, question='What')

    return HttpResponse("Query: %s" % query )
