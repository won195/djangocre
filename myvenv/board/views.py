from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Answer
from .forms import PostForm

def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'board/post_detail.html', context)

def answer_create(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    answer = Answer(post=post, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()    
    return redirect('board:detail', post_id=post.id)

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