from django.shortcuts import render
#from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_blogpost.html'
    fields = '__all__'
