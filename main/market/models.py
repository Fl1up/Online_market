from django.db import models
from django.utils import timezone
from rest_framework.reverse import reverse


# Create your models here.

class BaseModel(models.Model):
    """Information company"""
    name = models.CharField(max_length=100, verbose_name="Название")
    contacts = models.CharField(max_length=100, verbose_name="Контакты")
    email = models.EmailField(max_length=100, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    number_house = models.CharField(max_length=100, verbose_name="Номер дома")
    """Information products"""
    name_product = models.CharField(
        max_length=100, verbose_name="Название продукта")
    model_product = models.CharField(max_length=100, verbose_name="Модель")
    date_exit_product = models.DateTimeField(
        verbose_name="Дата выхода продукта")
    creation_time = models.CharField(
        default=timezone.now,
        verbose_name="Время создания заявки")

    def __str__(self):
        return f"{self.name},{self.model_product},{self.date_exit_product}"

    class Meta:
        verbose_name = "Базовый класс"
        verbose_name_plural = "Базовые классы"


class Factory(BaseModel):
    supplier = models.CharField(max_length=100, verbose_name="Поставщик")
    debt = models.CharField(default=0, verbose_name="Задолженность")

    def __str__(self):
        return f"{self.supplier}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"

    def get_provider_url(self):
        return reverse('admin:app_provider_change',
                       args=[str(self.supplier.id)])


class Retail(BaseModel):
    supplier = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        verbose_name="Поставщик")
    debt = models.CharField(default=0, verbose_name="Задолженность")

    def __str__(self):
        return f"{self.supplier},{self.debt}"

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class Ip(BaseModel):
    supplier = models.ForeignKey(
        Factory,
        on_delete=models.CASCADE,
        verbose_name="Поставщик")
    debt = models.CharField(default=0, verbose_name="Задолженность")

    def __str__(self):
        return f"{self.supplier},{self.debt}"

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"
