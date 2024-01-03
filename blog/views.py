from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
from ChatterBot import ChatBot 
from chatterbot.trainers import ListTrainer

def index(request):
    return render(request,'blog/index.html')
def specific(request):
    return HttpResponse("this is the specific url")
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)

