from django.http import HttpResponse

from .models import Question


def index(request):
    """
    最新の5つの質問を表示するView
    :param request: ユーザからのリクエストオブジェクト
    :return:
    """
    # order_by()でソートできる．ここではpub_dateカラムについて降順にソートし，上から5つ取得している．
    # 降順にするにはカラム名の先頭に'-'をつける
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 得られた質問オブジェクトの質問文を','区切りで出力
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    """
    質問の詳細ページのView
    :param request: ユーザからのリクエストオブジェクト
    :param question_id: 指定された質問のid
    """
    return HttpResponse("You're looking at question %s." % question_id)


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
