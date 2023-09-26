from django.urls import path

from .views import AdvertList

urlpatterns = [
    path('api/advert-list', AdvertList.as_view({'get': 'list'})),
    path('api/advert/<int:pk>/', AdvertList.as_view({"get": "retrieve"})),
]
