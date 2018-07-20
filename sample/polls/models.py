import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    質問のモデル
    """
    # CharFieldはmax_lengthが必須
    question_text = models.CharField(max_length=200)  # 質問文のカラム
    # 引数を与えるとAdminで表示時のカラム名として使われる
    pub_date = models.DateTimeField('date published')  # 作成された日付のカラム

    def was_published_recently(self) -> bool:
        """
        昨日より後に作成されたかどうかを判定するメソッド
        :return:
        """
        # timezone.now() -> 指定されたタイムゾーンでの現在時間を返す
        # datetime.timedelta(days=1) -> 1日分の時間を示す．これを引くことで1日前の時間を取得する．
        # 1日前から現在までの場合のみTrueを返す
        now = timezone.now()
        yday = now - datetime.timedelta(days=1)
        return yday <= self.pub_date <= now

    # 並び替える際に使用するフィールド
    was_published_recently.admin_order_field = 'pub_date'
    # 表示形式をBooleanにする
    was_published_recently.boolean = True
    # 表示名を変更
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        """表示名を質問文に"""
        return self.question_text


class Choice(models.Model):
    """
    選択肢のモデル
    """
    # 外部キー制約．on_deleteは必須パラメータ．ここではChoiceからQuestionへone to manyのリレーションを張っている.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 対応する質問のidを格納するカラム
    choice_text = models.CharField(max_length=200)  # 選択肢の文章
    # 初期値をdefaultで与えることが出来る
    votes = models.IntegerField(default=0)  # 投票数のカラム

    def __str__(self):
        """表示名を選択肢の文章に"""
        return self.choice_text
