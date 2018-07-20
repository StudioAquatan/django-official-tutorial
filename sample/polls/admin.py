from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """Question側からもChoiceを触れるようにする"""
    model = Choice
    # 表示数として最低3こぶん以上用意する
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """質問のAdminサイトでの表示をカスタマイズするクラス"""
    # 表示するフィールドをセクションごとに分ける
    fieldsets = [
        # セクション名無し
        (None, {'fields': ['question_text']}),
        # セクション名有り
        ('Date information', {'fields': ['pub_date']})
    ]
    # 表示項目を設定
    inlines = [ChoiceInline]


# Questionをadminサイトから触れるように登録
admin.site.register(Question, QuestionAdmin)
