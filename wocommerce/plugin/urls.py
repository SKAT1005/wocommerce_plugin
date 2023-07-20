from django.urls import path

from .views import CreateOrderView, CreateApiView

urlpatterns = [
    path('', CreateOrderView.as_view()),
    path('api/', CreateApiView.as_view())
]
