from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Answer
# Create your views here.



def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list }
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = { 'post' : post }
    return render(request, 'board/post_detail.html', context)

def answer_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('board:detail', post_id=post.id)