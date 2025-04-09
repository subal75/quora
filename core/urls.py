from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question-list'),
    path('new/', views.QuestionCreateView.as_view(), name='question-create'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    path('<int:pk>/answer/', views.AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:pk>/like/', views.LikeAnswerView.as_view(), name='like-answer'),
]