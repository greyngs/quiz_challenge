from django.shortcuts import render, redirect
from API.models import Question, Answer, History
from django.contrib import messages
import random

# Main view for the game, get random questions and their answers
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

# When the user responds
def step(request):
    code = request.POST['radio']

    answer = Answer.objects.get(pk=code)
    level = answer.questionId.level

    if answer.state == True:        # Win or next question
        if level == 5:              # Win
            record(level, request.user)
            messages.success(request, f'Congratulations!! {request.user.username} your won : {level * 1000} Dogecoins!!')
            return redirect('/')
        else:
            return redirect('/game/'+str(level+1))
    else:
        return redirect('/')

# Add the record to history
def record(level, user):
    score = level * 1000
    history = History.objects.create(
        user=user, score=score
    )

# When the user stays
def retire(request, level):
    score = level -1
    record(score, request.user)
    messages.success(request, f'{request.user.username} your score is saved : {score} Dogecoins!! - Play again ;)')
    
    return redirect('/')

# User is running out of time
def failTime(request):
    messages.success(request, f'{request.user.username} your time expired, you won : 0 Dogecoins!! - Play again ;)')
    
    return redirect('/')