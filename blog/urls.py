from django.urls import path
from .views import PostList, PostDetail, AddPost, EditPost, DeletePost


urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete_post/', DeletePost.as_view(), name='delete_post'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
