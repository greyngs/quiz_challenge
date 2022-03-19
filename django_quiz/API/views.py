from django.http import JsonResponse
from .models import Question, Answer
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import random
import json

class QuestionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            questions = list(Question.objects.filter(id=id).values())
            if len(questions) > 0:
                question = questions[0]
                datos = {'message':"Success", 'question':question}
            else:
                datos = {'message':"question not found..."}
            return JsonResponse(datos)
        else:
            questions = list(Question.objects.values())
            if len(questions)>0:
                datos = {'message':"Success", 'questions':questions}
            else:
                datos = {'message':"Questions not found..."}
            return JsonResponse(datos)

class RandomQuestionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, level=0):
        questions = list(Question.objects.filter(level=level).values())
        r = random.randint(0, len(questions)-1)
        if len(questions) > 0:
            question = questions[r]
            datos = {'message':"Success", 'question':question}
        else:
            datos = {'message':"question not found..."}
        return JsonResponse(datos)

class AnswerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, question=0):
        answers = list(Answer.objects.filter(questionId=question).values())
        if len(answers) > 0:
            datos = {'message':"Success", 'answers':answers}
        else:
            datos = {'message':"question not found..."}
        return JsonResponse(datos)
