from rest_framework import serializers

from .models import Advert, Category, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Advert
        fields = ["id", "title", "description", "city", "category", "views"]
