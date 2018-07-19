from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    """
    最新の5つの質問を表示するView
    :param request: ユーザからのリクエストオブジェクト
    :return:
    """

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 'latest_question_list'という名前で質問一覧をテンプレートエンジンに渡す
    context = {
        'latest_question_list': latest_question_list,
    }
    # loaderとHttpResponseを使わなくてもrenderというショートカットを利用できる
    # 第一引数にリクエストオブジェクト，第二引数が使用するテンプレート，第三引数がテンプレートエンジンに渡す変数
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    質問の詳細ページのView
    :param request: ユーザからのリクエストオブジェクト
    :param question_id: 指定された質問のid
    """
    # get_object_or_404の第一引数は取得するモデル，そこからカラム名と値で絞り込む．
    # Questionオブジェクトのidがquestion_idのものを探索．存在しない場合404を返す．
    # このショートカットを使うメリットはView側でエラーハンドリングしてメッセージを返す必要がなくなり，
    # Modelのmanagerのget()メソッドにおいてのエラーハンドリングのみで済むため，ViewとModelが分離できること
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    質問の結果ページのView
    :param request: ユーザからのリクエストオブジェクト
    :param question_id: 指定された質問のid
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


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
