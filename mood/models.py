from django.db import models

# Create your models here.

class Person(models.Model):
    wellbeing = models.IntegerField()

class Mood(models.Model):
    user = models.ForeignKey(Person, on_delete=models.PROTECT, default=None)
    date = models.DateTimeField(default=None)
    time = models.IntegerField(default=None, choices = [(i,i) for i in range(3)])
    value = models.IntegerField(choices = [(i,i) for i in range(6)], default=None)
    
class Answers(models.Model):
    user = models.ForeignKey(Person, on_delete=models.PROTECT, default=None)
    answer = models.IntegerField(choices = [(i,i) for i in range(2)], default=None)

class Questions(models.Model):
    influence = models.IntegerField(default=None)
    time = models.IntegerField(choices = [(i,i) for i in range(3)], default=None)
    question_text = models.CharField(max_length=255, default=None)
