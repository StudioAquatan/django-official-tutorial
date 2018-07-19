from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


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
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """
    投票ページのView
    :param request: ユーザからのリクエストオブジェクト
    :param question_id: 指定された質問のid
    """
    return HttpResponse("You're voting on question %s." % question_id)
