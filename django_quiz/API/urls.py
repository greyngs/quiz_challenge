from django.urls import path
from .views import QuestionView, RandomQuestionView, AnswerView

urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions_process'),
    path('questions/<int:id>', QuestionView.as_view(), name='questions_process'),
    path('randomquestion/<int:level>', RandomQuestionView.as_view(), name='rquestion_process'),
    path('answers/<int:question>', AnswerView.as_view(), name='answer_process')
]