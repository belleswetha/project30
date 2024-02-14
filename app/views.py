from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insertion_topic(request):
    ETFO = TopicForm()
    d={'ETFO':ETFO}
    if request.method=="POST":
        TFOO=TopicForm(request.POST)
        if TFOO.is_valid():
           TFOO.save()
           return HttpResponse('data is inserted')
    
    return render(request,'insertion_topic.html',d)



def insertion_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=="POST":
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
           WFDO.save()
           return HttpResponse('data is inserted')
    return render(request,'insertion_webpage.html',d)


def insertion_acess(request):
    EARFO=AcessRecordsForm()
    d={'EARFO':EARFO}
    if request.method=="POST":
        ARFDO=AcessRecordsForm(request.POST)
        if ARFDO.is_valid():
           ARFDO.save()
           return HttpResponse('data is inserted')
    return render(request,'insertion_acess.html',d)


        