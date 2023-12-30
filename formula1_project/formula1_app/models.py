from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Team(BaseModel):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    team_principal = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(BaseModel):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Race(BaseModel):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Result(BaseModel):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
    best_lap_time = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f"{self.race.title} - {self.driver.name} - Position: {self.position}"

class Championship(BaseModel):
    name = models.CharField(max_length=100)
    season_start = models.DateField()
    season_end = models.DateField()
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)
    races = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.name