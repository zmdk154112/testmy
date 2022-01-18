from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


def index(request):
    postList = Post.objects.order_by('-date')
    context = {'postList': postList} # 데이터베이스로부터 조회된 Queryset 을 Dictionary로 변환
    return render(request, 'board/list.html', context) # context에있는Post 모델 데이터 postList를 board/list.html 파일에 적용하여 HTML 코드로 변환 render(request, templatefile, 사전형객체)


def detail(request, postID):
    post = Post.objects.get(id=postID)
    context = {'post': post}
    return render(request, 'board/detail.html', context)


def answer_create(request, postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)# Post 모델에서 urls.py 로부터 전달받은 postId 와 동일한 키를 가지는 데이터를 받아와 post 객체에 저장
    post.answer_set.create(content=request.POST.get('content'), date=timezone.now()) # Answer 모델 데이터 생성, post를 pk로 가지는 answer 모델 반환, (Answer 모델이 Post 모델을 참조하고 있으므로 가능)
    return redirect('board:detail', postId=postId) # Form에서 POST된 데이터 중 name이 content인 엘리먼트가 가지는 값(답글 내용)