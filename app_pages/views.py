from django.shortcuts import render
from django.http import HttpResponse
from .models import Text

def index(request):
    latest_text_list = Text.objects.order_by('id')[:3]
    #output = ', '.join([t.text for t in latest_text_list])
    context = {
        'latest_text_list': latest_text_list,
    }
    return render(request, 'app_pages/index.html', context)

def detail(request, text_id):
    response = "You're looking at the TEXT %s."
    return HttpResponse(response % text_id)
