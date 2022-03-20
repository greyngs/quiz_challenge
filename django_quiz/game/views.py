from django.shortcuts import render, redirect
from API.models import Question, Answer, History
import random

def game(request, level=0):

    questions = list(Question.objects.filter(level=level).values())
    if len(questions) > 0:
        r = random.randint(0, len(questions)-1)
        question = questions[r]
    
    money = (level-1)*1000
    nextMoney = money + 1000

    answers = list(Answer.objects.filter(questionId=question["id"]).values())


    context = {'title' : "game", 'level' : level, 'question' : question, 'answers' : answers, 'money' : money, 'nextMoney' : nextMoney}
    return render(request, 'game.html', context)

def step(request):
    code = request.POST['radio']

    answer = Answer.objects.get(pk=code)
    level = answer.questionId.level

    if answer.state == True:
        if level == 5:
            record(level, request.user)
            return redirect('/')
        else:
            return redirect('/game/'+str(level+1))
    else:
        return redirect('/')

def record(level, user):
    score = level * 1000
    history = History.objects.create(
        user=user, score=score
    )

def retire(request, level):
    record(level, request.user)
    return redirect('/')