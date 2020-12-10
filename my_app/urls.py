from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.order_list, name='order_list'),
    re_path(r'^order/new/$', views.order_new, name='Order_new'),
]
