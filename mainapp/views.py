from django.shortcuts import render
from django.http import HttpRequest
from .models import ProductCategory, Product
import datetime

def index(request: HttpRequest):
    title = 'главная'

    products_list = [
        {
            'name': 'Отличный стул',
            'desc': 'Расположитесь комфортно.',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2'
        },
    ]

    return render(request, 'mainapp/index.html', {
        'title': title,
        'products': products_list
    })


def products(request: HttpRequest):
    title = 'продукты'

    links_menu = [
        {'href': '/products/0/', 'name': 'все'},
        {'href': '/products/1/', 'name': 'дом'},
        {'href': '/products/2/', 'name': 'офис'},
        {'href': '/products/3/', 'name': 'модерн'},
        {'href': '/products/4/', 'name': 'классика'},
    ]

    same_products = [
        {
            'name': 'Отличный стул',
            'desc': 'Не оторваться.',
            'image_src': 'product-11.jpg',
            'alt': 'продукт 11'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Комфортно.',
            'image_src': 'product-21.jpg',
            'alt': 'продукт 21'
        },
        {
            'name': 'Стул премиального качества',
            'desc': 'Просто попробуйте.',
            'image_src': 'product-31.jpg',
            'alt': 'продукт 31'
        },
    ]

    return render(request, 'mainapp/products.html', {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    })


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


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

