from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length = 200)    #varchar(200)이란뜻
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #pk는 디폴트값으로 id Auto_increment  로 사용중 Question의 참조클라스가 id
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content
