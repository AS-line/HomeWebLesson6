from django.shortcuts import render
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    berriers_arr = []
    fruits_and_veg = []
    i = 0
    for j in Product.objects.all():
        if j.catalog_id == 3:
            berriers_arr.append(j)
        if j.catalog_id == 1 or j.catalog_id == 2:
            fruits_and_veg.append(j)
        i += j.count

    context = {
        'all_products': Product.objects.all(),
        "all_count": i,
        "berriers_arr": berriers_arr,
        "fruits_and_veg": fruits_and_veg,
    }

    return render(request, 'index.html', context)
