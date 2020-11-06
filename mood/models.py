from django.db import models

# Create your models here.
class Mood(models.Model):
    mood_text = models.CharField(max_length=30)
