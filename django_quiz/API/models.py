from django.db import models

class Question(models.Model):
    level = models.IntegerField()
    body = models.CharField(max_length=120)

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)
    state = models.BooleanField()
