from django.db import models


class Question(models.Model):
    """
    質問のモデル
    """
    # CharFieldはmax_lengthが必須
    question_text = models.CharField(max_length=200)  # 質問文のカラム
    # 引数を与えるとAdminで表示時のカラム名として使われる
    pub_date = models.DateTimeField('date published')  # 作成された日付のカラム

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
