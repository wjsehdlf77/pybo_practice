from webbrowser import get
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Question
from django.utils import timezone


def index(request):
    # print(request)
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('create_date')
    #print(question_list)
    context = {
        'question_list' : question_list
        
    }

    #return HttpResponse('<h>안녕하세요</h>')
    return render(request, 'pybo/question_list.html', context)
    #HttpResponse를 반환

def detail(request, question_id):
    """
    pybo내용출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question' : question
    }
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                    create_date=timezone.now())                     #insert해라
    return redirect('pybo:detail', question_id=question.id)

#answer_set fk설정 부모 모델에 자동으로 생성
