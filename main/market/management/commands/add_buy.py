from django.core.management import BaseCommand
from django.utils import timezone

from main.market.models import Factory, Retail, Ip


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Factory.objects.all().delete()
        Retail.objects.all().delete()

        factory_1 = Factory.objects.create(
            name="Завод электроники",
            contacts="7-700",
            email="electro_omsk@mail.ru",
            country="Россия",
            city="Омск",
            number_house=12,
            name_product="Телевизоры",
            model_product="Электроника",
            date_exit_product="2023-10-25 07:08:40.736919+00:00",
            creation_time="2023-10-25 07:08:40.736919+00:00",
            supplier="Завод электроники",
            debt=0,
        )
        factory_2 = Factory.objects.create(
            name="Завод посуды",
            contacts="7-900",
            email="farfor_msk@mail.ru",
            country="Россия",
            city="Москва",
            number_house=119,
            name_product="Тарелки",
            model_product="Посуда",
            date_exit_product="2023-12-25 07:08:40.736919+00:00",
            creation_time="2023-11-25 07:08:40.736919+00:00",
            supplier="Завод посуды",
            debt=0,
        )
        Retail.objects.create(
            name="ооо МосПосуда",
            contacts="7-600",
            email="farfor_msk@mail.ru",
            country="Россия",
            city="Москва",
            number_house=119,
            name_product="Тарелки",
            model_product="Посуда",
            date_exit_product="2023-12-25 07:08:40.736919+00:00",
            creation_time="2023-11-25 07:08:40.736919+00:00",
            supplier=factory_1,
            debt=200,
        )
        Ip.objects.create(
            name="Ип Орехов.О",
            contacts="7-790",
            email="ip_orex@mail.ru",
            country="Россия",
            city="Воронеж",
            number_house=19,
            name_product="Телевизор",
            model_product="Электроника",
            date_exit_product="2023-12-25 07:08:40.736919+00:00",
            creation_time="2023-11-25 07:08:40.736919+00:00",
            supplier=factory_2,
            debt=100.5,
        )
