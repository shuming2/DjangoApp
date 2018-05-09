from django.shortcuts import render

from .models import Question, Answer, User


def quiz(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'quiz.html', context)


def submit(request):
    question_list = Question.objects.all()
    user = User.objects.create()

    for q in question_list:
        input_name = 'answer'+str(q.id)
        input_answer = request.POST[input_name]
        answer = Answer.objects.create(question=q, answer_text=input_answer, user=user)
        answer.save()

    return render(request, 'formResponse.html', {})


def result(request):
    question_list = Question.objects.all()
    user_list = User.objects.order_by('-date')
    context = {'question_list': question_list, 'user_list': user_list}
    return render(request, 'result.html', context)


def question(request, pk):
    q = Question.objects.get(id=pk)
    answer_list = Answer.objects.filter(question_id=pk).order_by('-user__date')
    context = {'answer_list': answer_list, 'question': q}
    return render(request, 'answer.html', context)


def session(request, pk):
    user = User.objects.get(session=pk)
    answer_list = Answer.objects.filter(user__session=pk)
    context = {'answer_list': answer_list, 'user': user}
    return render(request, 'session.html', context)
