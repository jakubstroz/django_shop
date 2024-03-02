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
    categories_query = Category.objects.all()
    
    try:
        query = Product.objects.get(pk=id)
    except:
        query = 'Nie ma produktu o takim id'

    query.price /= 100
    
    data = {'one_product': query, 'categories': categories_query}
    return render(request, 'product.html', data)


def categories(request):
    query = Category.objects.all()
    data = {'kategorie': query}
    return render(request,'template.html',data)

def one_category(request, id):
    categories_query = Category.objects.all()
    query = Category.objects.get(pk=id) 
    products_query = Product.objects.filter(category=query)
    data = {'one_category':query, 'products': products_query, 'categories': categories_query}
    return render(request, 'category.html', data)