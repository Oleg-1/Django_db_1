from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User

from mainapp.models import ProductCategory
from authapp.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        # ProductCategory.objects.all().delete()
        #
        # for x in range(5):
        #     new_cat = ProductCategory()
        #     new_cat.save()

        # User.objects.create_superuser(
        #     'manchenkov123', 'test@test.com', 'root'
        # )

        CustomUser.objects.create_superuser(
            'oleg', 'test@test.com', 'root', age=25
        )
