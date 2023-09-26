from django.db.models import F
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Advert
from .serializers import AdvertSerializer


class AdvertList(viewsets.ViewSet):
    queryset = (Advert.objects.all()
                .select_related("city")
                .prefetch_related("category"))

    def list(self, request):  # noqa

        serializer = AdvertSerializer(self.queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk: int = None):  # noqa
        advert = get_object_or_404(self.queryset, pk=pk)

        Advert.objects.filter(id=pk).update(views=F('views') + 1)

        serializer = AdvertSerializer(advert)

        return Response(serializer.data)
