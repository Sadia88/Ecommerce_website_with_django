from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
  
    return render(request,'shop/index.html')



def about(request):
   return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("contact")


def tracker(request):
    pass

def search(request):
    pass

def productview(request):
    pass


def checkout(request):
    pass