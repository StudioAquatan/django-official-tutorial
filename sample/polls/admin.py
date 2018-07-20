from django.contrib import admin

from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    """質問のAdminサイトでの表示をカスタマイズするクラス"""
    # 表示するフィールドをセクションごとに分ける
    fieldsets = [
        # セクション名無し
        (None, {'fields': ['question_text']}),
        # セクション名有り
        ('Date information', {'fields': ['pub_date']})
    ]


# QuestionとChoiceをadminサイトから触れるように登録
admin.site.register(Question, QuestionAdmin)
