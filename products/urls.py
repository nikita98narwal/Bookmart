from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^details/(?P<id>\d+)', details, name='details' ),
    ]