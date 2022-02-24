from ast import mod
from django.db import models


class Profile(models.Model):
    player_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    xp = models.BigIntegerField(default=0)
    gold = models.BigIntegerField(default=0)

