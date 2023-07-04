from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Answer
from django.http import HttpResponseNotAllowed
from .forms import PostForm, AnswerForm

def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'board/post_detail.html', context)

def answer_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('board:detail', post_id=post.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'post': post, 'form': form}
    return render(request, 'board/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('board:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'board/post_form.html', context)