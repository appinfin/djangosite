from django.urls import path, re_path
from .views import *

# допустимые адреса

urlpatterns = [
    path('', index, name='home'),
    path('prod/<int:prodid>/', products),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]