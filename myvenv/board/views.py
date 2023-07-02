from django.shortcuts import render
from .models import Post
# Create your views here.



def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list }
    return render(request, 'board/post_list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = { 'post' : post }
    return render(request, 'board/post_detail.html', context)