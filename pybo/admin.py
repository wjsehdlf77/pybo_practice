from django.contrib import admin
from .models import Question
from .models import Answer


# Register your models here.     


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'create_date']

    

admin.site.register(Question, QuestionAdmin)        #admin사이트에 모델등록
admin.site.register(Answer)
