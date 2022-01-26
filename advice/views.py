from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic

from advice.models import Question


class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Question
    fields = ['title']
    success_message = "Question Created Successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Question
    success_message = "Question Deleted Successfully!"
    success_url = "/questions"

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(QuestionDeleteView, self).delete(request, *args, **kwargs)


class QuestionDetailView(generic.DetailView):
    model = Question


class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 3
    ordering = ['-date_published']
