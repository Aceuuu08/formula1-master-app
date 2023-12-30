from django.core.management.base import BaseCommand
from formula1_app.models import Team, Driver, Race, Result, Championship
from datetime import date

class Command(BaseCommand):
    help = 'Creates initial data for the F1 application'

    def handle(self, *args, **kwargs):
        self.create_f1_data()

    def create_f1_data(self):
        # Create Teams
        team1 = Team(name="Mercedes", country="Germany", team_principal="Toto Wolff")
        team1.save()

        team2 = Team(name="Ferrari", country="Italy", team_principal="Mattia Binotto")
        team2.save()

        team3 = Team(name="McLaren", country="United Kingdom", team_principal="Zak Brown")
        team3.save()

        team4 = Team(name="Red Bull Racing", country="Austria", team_principal="Christian Horner")
        team4.save()

        team5 = Team(name="Alpine", country="France", team_principal="Davide Brivio")
        team5.save()

        team6 = Team(name="Aston Martin", country="United Kingdom", team_principal="Otmar Szafnauer")
        team6.save()

        team7 = Team(name="Alfa Romeo Racing", country="Switzerland", team_principal="Frédéric Vasseur")
        team7.save()

        team8 = Team(name="Williams", country="United Kingdom", team_principal="Jost Capito")
        team8.save()

        team9 = Team(name="Haas F1 Team", country="United States", team_principal="Günther Steiner")
        team9.save()

        team10 = Team(name="AlphaTauri", country="Italy", team_principal="Franz Tost")
        team10.save()
        

        # Create Drivers
        driver1 = Driver(name="Lewis Hamilton", nationality="British", birth_date=date(1985, 1, 7), team=team1)
        driver1.save()

        driver2 = Driver(name="Sebastian Vettel", nationality="German", birth_date=date(1987, 7, 3), team=team2)
        driver2.save()

        # Create Races
        race1 = Race(title="Monaco Grand Prix", date=date(2023, 5, 28), location="Monaco")
        race1.save()

        race2 = Race(title="Italian Grand Prix", date=date(2023, 9, 3), location="Monza")
        race2.save()

        # Create Results
        result1 = Result(race=race1, driver=driver1, position=1, best_lap_time=75.345)
        result1.save()

        result2 = Result(race=race2, driver=driver2, position=2, best_lap_time=80.123)
        result2.save()

        championship1 = Championship(
            name="2023 F1 World Championship",
            season_start=date(2023, 1, 1),
            season_end=date(2023, 12, 31),
        )
        championship1.save()

        championship2 = Championship(
            name="2024 F1 World Championship",
            season_start=date(2024, 1, 1),
            season_end=date(2024, 12, 31),
        )
        championship2.save()


        self.stdout.write(self.style.SUCCESS('Successfully created initial F1 data.'))
