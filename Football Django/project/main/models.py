from django.db import models
from django_countries.fields import CountryField
from colorfield.fields import ColorField

class Championship(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
    theme_color = ColorField(default='#FF0000')
    achievements = models.ManyToManyField(Championship, through='Achievement')
    def __str__(self):
        return self.name

class Achievement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return f'{self.team.__str__()} - {self.championship.__str__()} - {self.date}'

class Message(models.Model):
    name = models.CharField(max_length=80)
    message = models.CharField(max_length=500)
    date = models.DateField()
    favTeam = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} - {self.message}'