from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'qwer', 'description': 'asdf', 'created_at': '2002-08-14'},
            {'name': 'qwert', 'description': 'asdfg', 'created_at': '2002-08-15'},
            {'name': 'qwery', 'description': 'asdfh', 'created_at': '2002-08-16'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
        print(category_for_create)