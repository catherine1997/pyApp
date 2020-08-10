from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from .models import Choice, Question


class IndexView(generic.ListView):
	template_name='poll/index.html'
	context_object_name='latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions"""
		return Question.object.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'poll/detail.html'	


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'poll/results.html'



	def vote(request, question_id):
		model = Question
		template_name = 'poll/vote.html'
	