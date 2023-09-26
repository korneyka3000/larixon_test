from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Город')

    class Meta:
        db_table = 'city'

    def __str__(self):
        return f"{self.name}"


class Advert(models.Model):
    title = models.CharField(max_length=255, verbose_name='Объявление')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_ads')
    category = models.ManyToManyField(Category, related_name="category_ads")
    views = models.PositiveIntegerField(default=0, verbose_name="Кол-во просмотров")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    class Meta:
        db_table = 'advert'

    def __str__(self):
        return f"{self.title}"
