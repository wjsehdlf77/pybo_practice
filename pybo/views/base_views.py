from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question





def index(request):
    # print(request)
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    #print(question_list)
    total_count = Question.objects.count()
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'question_list' : page_obj,
        'total_count' : total_count
        
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