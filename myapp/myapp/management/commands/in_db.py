#!/usr/bin/env python
from django.core.management.base import BaseCommand
from myapp.myapp.models.models import MyShop, Type, Category, SubCategory, LiveSales, Sails
from myapp.authapp.models import ShopUser
import json
import os

JSON_PATH = 'myapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON("categories")
        MyShop.objects.all().delite()
        for categories in categories:
            print(categories)
