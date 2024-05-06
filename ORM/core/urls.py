from django.urls import path
from .views import index, order_form
urlpatterns = [
    path('', index, name='index'),
    path('order_form/', order_form, name='order_form'),
]
