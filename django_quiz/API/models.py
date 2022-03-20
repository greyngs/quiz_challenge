from django.db import models
from django.conf import settings
from datetime import datetime

class Question(models.Model):
    level = models.IntegerField()
    body = models.CharField(max_length=120)

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    state = models.BooleanField()

class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)