
from django.urls import path

from entertainments.views import contato, home, sobre

urlpatterns = [
    path('contato/', contato),
    path('', home),
    path('sobre/', sobre),
]
