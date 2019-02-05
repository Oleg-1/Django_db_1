from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from basketapp.models import Basket

import datetime
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404


def main(request: HttpRequest):
    title = 'главная'

    products = Product.objects.all()


    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products,
    })


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)


def product_detail(request: HttpRequest, id=None):
    item = get_object_or_404(Product, pk=id)
    same_products = Product.objects.exclude(pk=id).filter(category__pk=item.category_id)
    links_menu = ProductCategory.objects.all()

    context = {
        'title': f'Товар: {item.name}',
        'item': item,
        'products': same_products,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/details.html', context)


def contact(request: HttpRequest):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]

    return render(request, 'mainapp/contact.html', {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    })
