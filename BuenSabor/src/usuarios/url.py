from django.urls import re_path
from . import views

app_name = 'usuarios_app'

urlpatterns = [

    re_path('api/clientes/$', views.cliente_list),
    re_path('api/clientes/(?P<pk>[0-9]+)$', views.cliente_detail),
]
