from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request):
    categories_query = Category.objects.all()
    products_query = Product.objects.all()

    categories_data = {'categories': categories_query}
    products_data = {'products': products_query}
    return render(request, 'template.html', categories_data)


def one_product(request, id:int):
    query = Product.objects.get(pk=id)
    output = f"""<h1> {query.category if query.category is not None else ''} </h1>
                <h1>{query.producer} - {query.name} </h1>
                <p>OPIS: {query.description} </p>
                <p>CENA: {str(query.price)} </p>
"""
    return HttpResponse(output)


def categories(request):
    #query = Category.objects.get(pk=id) 
    #return HttpResponse(query.name)
    query = Category.objects.all()
    data = {'kategorie': query}
    return render(request,'template.html',data)

def one_category(request, id):
    query = Category.objects.get(pk=id) 
    return HttpResponse(query.name)