from django.shortcuts import render
from .models import Order
from .forms import *


def first_page(request):
    form = OrderForm()
    orders = Order.objects.all()
    return render(request, './index.html', {'orders': orders, 'form': form})


def thanks(request):
    name = request.POST['name']
    number = request.POST['number']
    element = Order(name=name, number=number)
    element.save()
    return render(request, './thanks.html', {'name': name, 'number': number})
