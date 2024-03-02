from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request):
    query = Product.objects.all()
    return HttpResponse(query)


def one_product(request, id:int):
    query = Product.objects.get(pk=id)
    output = f"""<h1> {query.category if query.category is not None else ''} </h1>
                <h1>{query.producer} - {query.name} </h1>
                <p>OPIS: {query.description} </p>
                <p>CENA: {str(query.price)} </p>
"""
    return HttpResponse(output)


def categories(request, id:int):
    query = Category.objects.get(pk=id) 
    return HttpResponse(query.name)