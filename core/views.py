from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Question, Answer
from .forms import RegisterForm, QuestionForm, AnswerForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('question-list')
        return render(request, 'home.html')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('question-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'
    ordering = ['-created_at']
    paginate_by = 10

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'question_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm()
        return context

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'question_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('question-detail', kwargs={'pk': self.kwargs['pk']})

class LikeAnswerView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        answer = get_object_or_404(Answer, pk=kwargs['pk'])
        if request.user in answer.likes.all():
            answer.likes.remove(request.user)
        else:
            answer.likes.add(request.user)
        return HttpResponseRedirect(reverse_lazy('question-detail', kwargs={'pk': answer.question.pk}))