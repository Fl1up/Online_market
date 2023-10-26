from django.core.management import BaseCommand

from main.users.models import User


class Command(BaseCommand):
    User.objects.all().delete()

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email="admin@sky.pro",
            first_name="Admin",
            last_name="SkyPro",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        user.set_password("123")
        user.save()

        user = User.objects.create(
            email="german@sky.pro",
            first_name="Admins",
            last_name="SkyPro1",
            is_staff=True,
            is_superuser=True,
            is_active=False,
        )

        user.set_password("123")
        user.save()
