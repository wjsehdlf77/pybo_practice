print('hello')


from pybo.models import Question
from django.utils import timezone

for i in range(300):
    q = Question(subject = f'테스트 데이터 : {i:03d}', content = '내용물', create_date = timezone.now())
    q.save()


