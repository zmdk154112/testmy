from django.urls import path
from . import views

app_name = 'board' # 네임스페이스

urlpatterns = [
    path('', views.index, name='index'), # /board-->index 라는 별칭
    path('<int:postID>/', views.detail), # /board/{{post.id}}-->detail 이라는 별칭
    path('answer/create/<int:postId>/', views.answer_create, name='answer_create'),
]