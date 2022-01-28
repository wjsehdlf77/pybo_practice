from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Question
# Create your views here.
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
