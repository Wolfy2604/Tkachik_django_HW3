from django.forms import model_to_dict
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')
    context = {}
    if sort_type == 'name' or not sort_type:
        context = {
            'phones': Phone.objects.order_by('name')
        }
    elif sort_type == 'min_price':
        context = {
            'phones': Phone.objects.order_by('price')
        }
    elif sort_type == 'max_price':
        context = {
            'phones': Phone.objects.order_by('-price')
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
