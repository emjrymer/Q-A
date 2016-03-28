from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, TemplateView, DetailView, View
from django.http import HttpResponseRedirect
from rest_framework import generics
from app.models import Question, Answer, UserProfile, Vote
from app.serializers import QuestionSerializer, AnswerSerializer


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login_view")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.all()[:5]
        return context


class MyProfileView(DetailView):
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_questions'] = Question.objects.filter(user=self.request.user)
        context['user_answers'] = Answer.objects.filter(user=self.request.user)
        return context

class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(related_question=self.kwargs.get('pk'))
        context['ans_id_list'] = []
        for answer in context['answers']:
            if answer.user == 'auth.User':
                context['ans_id_list'].append(answer.id)
        print(context)
        return context


class QuestionCreateView(CreateView):
    model = Question
    fields = ('title', 'body', 'tag')

    def form_valid(self, form):
        question_instance = form.save(commit=False)
        question_instance.user = self.request.user
        question_instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index_view')


class AnswerCreateView(CreateView):
    model = Answer
    fields = ('body',)

    def form_valid(self, form):
        ans_instance = form.save(commit=False)
        ans_instance.related_question = Question.objects.get(pk=self.kwargs.get('q_id'))
        ans_instance.user = self.request.user
        ans_instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index_view')


def down_vote(request, **kwargs):
    Vote.objects.create(answer=Answer.objects.get(id=kwargs['a_id']), user=request.user.profile, vote_choice="down")
    return HttpResponseRedirect('/')

def up_vote(request, **kwargs):
    Vote.objects.create(answer=Answer.objects.get(id=kwargs['a_id']), user=request.user.profile, vote_choice="up")
    return HttpResponseRedirect('/')
