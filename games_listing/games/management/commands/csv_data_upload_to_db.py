from django.core.management import BaseCommand


import pandas as pd
from ...models import Game


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Using pandas creating the records in the db from csv
        data = pd.read_csv("gamesc2b2088.csv")

        games = list()
        for index, row in data.iterrows():
            games.append(Game(**row))

        Game.objects.bulk_create(games)



