from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import uuid

from .models import Question, Answer, User


def quiz(request):
    question_list = Question.objects.all().order_by('id')
    context = {'question_list': question_list}
    return render(request, 'quiz.html', context)


def submit(request):
    question_list = Question.objects.all()
    user = User.objects.create(session=uuid.uuid4())

    for q in question_list:
        input_name = 'answer'+str(q.id)
        input_answer = request.POST[input_name]
        answer = Answer.objects.create(question=q, answer_text=input_answer, user=user)
        answer.save()

    return render(request, 'formResponse.html', {})


@login_required(login_url='/admin/login/')
def result(request):
    question_list = Question.objects.all().order_by('id')
    user_list = User.objects.order_by('-date')
    context = {'question_list': question_list, 'user_list': user_list}
    return render(request, 'result.html', context)


@login_required(login_url='/admin/login/')
def question(request, pk):
    q = Question.objects.get(id=pk)
    answer_list = Answer.objects.filter(question_id=pk).order_by('-user__date')
    context = {'answer_list': answer_list, 'question': q}
    return render(request, 'answer.html', context)


@login_required(login_url='/admin/login/')
def session(request, pk):
    user = User.objects.get(session=pk)
    answer_list = Answer.objects.filter(user__session=pk).order_by('question_id')
    context = {'answer_list': answer_list, 'user': user}
    return render(request, 'session.html', context)
