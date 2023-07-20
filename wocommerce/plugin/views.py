import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View



from .forms import APIForm, OrderForm
from .models import API, Order


def add_new_oreder(order):
    url = order.api.apy_type.API_url
    data = {
        'api_key': order.api.API_key,
        'link': order.link,
        'service': order.servis_id,
        'quantity': order.quantity
    }
    response = requests.post(url, data=data)
    order_id = json.loads(response.text)['order']
    order.order_id = order_id
    order.save()
class CreateApiView(View):
    def get(self, request):
        form = APIForm
        return render(request, 'create_api.html', context={'form': form})

    def post(self, request):
        form = APIForm(request.POST)
        if form.is_valid():
            API.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'create_api.html', context={'form': form})

class CreateOrderView(View):
    def get(self, request):
        form = OrderForm
        return render(request, 'create_order.html', context={'form': form})

    def post(self, request):
        form = APIForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(**form.cleaned_data)
            add_new_oreder(order)
            return HttpResponseRedirect('/')
        return render(request, 'create_api.html', context={'form': form})