from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, response, Http404

from .models import Question
from .forms import QuestionForm
from django.utils import timezone

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, 'exercice1/index.html', {'questions': questions})

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return HttpResponseRedirect('/exercice1/')
    else:
        form = QuestionForm()
    return render(request, 'exercice1/create.html', {'form': form})

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'exercice1/details.html', {'question': question})

def update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return HttpResponseRedirect('/exercice1/')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'exercice1/update.html', {'form': form})

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return HttpResponseRedirect('/exercice1/')