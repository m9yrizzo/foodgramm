import csv
import os.path
import sys
import time

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    """
    Команда 'data_loader' загружает данные
    в БД из csv файла. Статичная директория «./data/».
    """

    help = 'load data from csv files'

    def handle(self, *args, **options):
        count = 0
        file = 'ingredients.csv'
        path = (os.path.join('./data/', file))
        with open(path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                id = count
                ingredients = Ingredient(
                    id=id,
                    name=row[0],
                    measurement_unit=row[1]
                )
                ingredients.save()
                count += 1
                print('\b' * 30, end='')
                print('Добавлено записей: {}'.format(count), end='')
                sys.stdout.flush()
                time.sleep(0.05)
        print('\n')
        print('Загрузка завершена.')
