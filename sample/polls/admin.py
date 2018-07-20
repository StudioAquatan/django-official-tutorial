from django.contrib import admin

from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    """質問のAdminサイトでの表示をカスタマイズするクラス"""
    # 表示するフィールドをセクションごとに分ける
    fieldsets = [
        # セクション名無し
        (None, {'fields': ['question_text']}),
        # セクション名有り
        ('Date information', {'fields': ['pub_date']})
    ]


# Questionをadminサイトから触れるように登録
admin.site.register(Question, QuestionAdmin)

# Choiceも登録する
# これでChoice側からQuestionとのリレーションを変更できる
admin.site.register(Choice)
