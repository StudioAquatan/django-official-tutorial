from django.contrib import admin

from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    """質問のAdminサイトでの表示をカスタマイズするクラス"""
    # 表示するフィールドの順番を変更
    fields = ['pub_date', 'question_text']


# QuestionとChoiceをadminサイトから触れるように登録
admin.site.register(Question, QuestionAdmin)
