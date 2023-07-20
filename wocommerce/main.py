import json

import requests
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wocommerce.settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
call_command('runserver',  '127.0.0.1:8000')
from plugin.models import Order


def get_status(order):
    data = {
        'order_id': order.order_id
    }
    url = order.api.apy_type.API_url
    response = requests.post(url, data=data)
    status = json.loads(response.text)['status']
    order.status = status
    order.save()


while True:
    orders = Order.objects.filter(status__in=['In progress'])
    for order in orders:
        if order.order_id:
            get_status(order)
