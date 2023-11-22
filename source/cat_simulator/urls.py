from django.urls import path
from cat_simulator.views import cat_info, start

urlpatterns = [
    path('', start),
    path('cat_stat/', cat_info)
]
