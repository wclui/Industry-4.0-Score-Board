from django.db import models

# Create your models here.
class scoreBoard(models.Model):
    team_name = models.CharField(max_length=128)
    team_score = models.IntegerField(null=True)
