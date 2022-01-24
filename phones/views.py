from django.forms import model_to_dict
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    qs = Phone.objects.all()
    phones = []
    for item in qs:
        print(type(item))
        phones.append(
            {
                'id': item['id'],
                'name': item['name'],
                'image': item['image'],
                'price': item['price'],
                'release_date': item['release_date'],
                'lte_exists': item['lte_exists'],
                'slug': item['name']
            }
        )
    context = {
        'qs': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
