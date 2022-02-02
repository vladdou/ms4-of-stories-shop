from django.urls import path
# from . import views
from .views import PostList, PostDetail, AddPost, EditPost


urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
