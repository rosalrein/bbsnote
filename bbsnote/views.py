from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator


def index(request):
    #입력인자
    page = request.GET.get('page', 1)
    #조회
    board_list = Board.objects.order_by('-create_date')
    #페이징처리
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}

    #return HttpResponse("bbsnote에 오신것을 환영합니다.");
    return render(request, 'bbsnote/board_list.html' , context)
'''
def index(request):
    board_list = Board.objects.order_by('-create_date')
    context = {'board_list' : board_list}
    #return HttpResponse("bbsnote에 오신것을 환영합니다.");
    return render(request, 'bbsnote/board_list.html' , context)
'''
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board' : board}
    return render(request, 'bbsnote/board_detail.html', context)

def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('bbsnote:index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})

'''
#데이터 저장 기본 문법
def comment_create(request, board_id):
    board = Board.object.get(id=board_id) #보드를 가져오는것
    comment = Comment(board=board, content=request.POST.get('content')), #comment는 게시판의 내용을 가져와라
    create_date = timezone.now() #시간은 현재시간으로 넣어줘라
    comment.save()
    return redirect('bbsnote:detail', board_id=board_id)
'''
#foreign_key로 연결이 되어있을경우에는 다음과 같이 데이터 저장을 할 수 있다
def comment_create(request, board_id):
    board = Board.objects.get(id=board_id) #보드를 가져오는것
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('bbsnote:detail', board_id=board.id)
