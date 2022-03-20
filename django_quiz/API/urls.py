from django.urls import path
from .views import QuestionView, RandomQuestionView, AnswerView

urlpatterns = [
    path('questions/', QuestionView.as_view(), name='questions_process'),
    path('question/<int:id>', QuestionView.as_view(), name='questions_process'),
    path('rquestion/<int:level>', RandomQuestionView.as_view(), name='rquestion_process'),
    path('answers/<int:question>', AnswerView.as_view(), name='answer_process')
]