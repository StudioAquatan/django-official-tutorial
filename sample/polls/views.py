from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# クラスベースビューの詳細は https://docs.djangoproject.com/ja/2.0/topics/class-based-views/
# ListViewは要素をリスト表示するための汎用View
class IndexView(generic.ListView):
    """
    最新の質問5つを表示するView．
    """
    # 使用するテンプレートを指定
    template_name = 'polls/index.html'
    # テンプレートで使用する変数名の指定
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        クエリセットを取得する関数をオーバーライドし，最新の質問5つを返す．
        """
        return Question.objects.order_by('-pub_date')[:5]


# DetailViewは指定したモデルの要素一つを取得し表示する汎用View
class DetailView(generic.DetailView):
    """
    質問の詳細ページのView
    """
    # 詳細を表示するモデルを指定
    model = Question
    # 使用するテンプレートを指定
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    """
    質問の結果ページのView
    """
    # 詳細を表示するモデルを指定
    model = Question
    # 使用するテンプレートを指定
    template_name = 'polls/results.html'


def vote(request, question_id):
    """
    投票ページのView
    :param request: ユーザからのリクエストオブジェクト
    :param question_id: 指定された質問のid
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POSTはPythonでいう辞書のようなオブジェクト
        # 'choice'フィールドがPOSTされなかった場合，KeyErrorが送出される
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 何も選択しなかった場合，投票した質問の詳細ページを表示する
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # その選択肢へ投票し，セーブする（DBへ反映する）．
        selected_choice.votes += 1
        selected_choice.save()
        # POSTに成功したらリダイレクトを返すのはWebアプリのお作法．今回の場合は結果ページへリダイレクトする．
        # reverseはURLの逆引きをする関数，'polls:results'に質問のidを渡したURLを取得することでurls.pyと実装を分離できる．
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
