from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Message

# Create your views here.

def index(request):
    #context = {'data':'message'}
    message_list = Message.objects.order_by('-key')[:1]
    context = {'message_list': message_list}

    return render(request, 'texts/index.html', context)

def detail(request, message_id):
    # message = Message.objects.get(pk=message_id)
    message = get_object_or_404(Message, pk=message_id)
    context = {'message': message}

    return render(request, 'texts/detail.html', context)
