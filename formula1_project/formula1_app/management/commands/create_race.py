from django.core.management.base import BaseCommand
from formula1_app.models import Team, Driver, Race, Result, Championship
from datetime import date

class Command(BaseCommand):
    help = 'Creates initial data for the F1 application'

    def handle(self, *args, **kwargs):
        self.create_f1_data()

    def create_f1_data(self):

        race2 = Race(title="Australian Grand Prix", date=date(2023, 3, 19), location="Melbourne")
        race2.save()

        race3 = Race(title="Bahrain Grand Prix", date=date(2023, 4, 2), location="Sakhir")
        race3.save()

        race4 = Race(title="Chinese Grand Prix", date=date(2023, 4, 9), location="Shanghai")
        race4.save()

        race5 = Race(title="Spanish Grand Prix", date=date(2023, 5, 14), location="Barcelona")
        race5.save()

        race6 = Race(title="Monaco Grand Prix", date=date(2023, 5, 28), location="Monaco")
        race6.save()

        race7 = Race(title="Canadian Grand Prix", date=date(2023, 6, 11), location="Montreal")
        race7.save()

        race8 = Race(title="British Grand Prix", date=date(2023, 7, 16), location="Silverstone")
        race8.save()

        race9 = Race(title="Belgian Grand Prix", date=date(2023, 8, 27), location="Spa-Francorchamps")
        race9.save()

        race10 = Race(title="Japanese Grand Prix", date=date(2023, 10, 8), location="Suzuka")
        race10.save()

        race11 = Race(title="United States Grand Prix", date=date(2023, 10, 22), location="Austin")
        race11.save()

        race12 = Race(title="Italian Grand Prix", date=date(2023, 9, 3), location="Monza")
        race12.save()


        self.stdout.write(self.style.SUCCESS('Successfully created initial F1 data.'))

