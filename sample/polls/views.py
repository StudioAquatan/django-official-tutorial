from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    """
    最新の5つの質問を表示するView
    :param request: ユーザからのリクエストオブジェクト
    :return:
    """

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 'polls/templates'以下にある'polls/index.html'を取得
    # 'templates'以下に直接ファイルを置くと，Djangoの他のアプリケーションが使用するtemplateと競合する可能性がある．
    template = loader.get_template('polls/index.html')
    # 'latest_question_list'という名前で質問一覧をテンプレートエンジンに渡す
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


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
