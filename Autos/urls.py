from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('autos/',autos,name='autos'),
    path('clientes/',clientes,name='clientes'),
]
