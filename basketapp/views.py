from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from mainapp.models import Product
from basketapp.models import Basket


@login_required
def add(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)

    exists_item = Basket.objects.filter(product__id=id, user=request.user)  # user_id

    if exists_item:
        exists_item[0].quantity += 1
        exists_item[0].save()
    else:
        new_item = Basket(user=request.user, product=product)
        new_item.quantity = 1
        new_item.save()

    if request.is_ajax():
        return JsonResponse({
            'quantity': Basket.objects.get(product__id=id).quantity
        })

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect('/products/details/' + str(product.id))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # SERVER VARS


@login_required
def remove(request: HttpRequest, id: int):  # /basket/remove/1
    item = get_object_or_404(Basket, pk=id)

    item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def index(request: HttpRequest):
    products = Basket.objects.filter(user=request.user)

    context = {
        'products': products
    }

    return render(request, 'basketapp/index.html', context)
