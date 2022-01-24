import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        some_phone = None
        for phone in phones:
            some_phone = Phone(id=phone['id'], name=phone['name'], image=phone['image'], \
                               price=phone['price'], release_date=phone['release_date'], \
                               lte_exists=phone['lte_exists'], slug=phone['name'])
            some_phone.save()
            print(f'{phone} занесен в базу')


