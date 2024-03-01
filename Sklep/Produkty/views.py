from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    query = Product.objects.all()
    return HttpResponse(query)

