from django.contrib import admin

from polls.models import Question

# QuestionとChoiceをadminサイトから触れるように登録
admin.site.register(Question)
