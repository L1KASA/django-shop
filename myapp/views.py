from django.http import Http404
from django.shortcuts import render

from myapp.exceptioins import ProductNotFoundException
from myapp.models import Product


def index(request):
    items = Product.objects.all()

    context = {'items': items}

    return render(request, "index.html", context)

def id_item(request, id):
    try:
        item = Product.objects.get(id=id)
    except ProductNotFoundException as e:
        raise Http404(str(e))
    context = {'item': item}
    return render(request, "phone.html", context)


