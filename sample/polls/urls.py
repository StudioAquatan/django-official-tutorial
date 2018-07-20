from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # `/polls/`
    path('', views.IndexView.as_view(), name='index'),
    # 注意：末尾のスラッシュを忘れないように
    # 汎用ビューを使用する場合，オブジェクト取得のためにそのオブジェクトのidをpk（primary keyの略）として指定する
    # `/polls/1/`
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # `/polls/1/results/`
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # `/polls/1/vote/`
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
