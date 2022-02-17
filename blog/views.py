from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Post

# code credits: https://djangocentral.com/building-a-blog-application-with-django/ 
# & https://www.youtube.com/watch?v=B40bteAMM_M

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPost(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'


class EditPost(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = '__all__'


class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
