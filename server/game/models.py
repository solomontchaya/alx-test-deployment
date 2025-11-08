from django.db import models

# Create your models here.
class Game(models.Model):
    player_name = models.CharField(max_length=100)
    secret_number = models.IntegerField()
    attempts = models.IntegerField(default=0)
    is_won = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player_name}'s game"