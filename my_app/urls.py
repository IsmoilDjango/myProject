from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from my_app.views import PostListCreateAPIView, PostDetailApiView, CommentCreateApiView
urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api/posts/', PostListCreateAPIView.as_view(), name='list-create'),
    path('api/posts/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
    path('comment/', CommentCreateApiView.as_view(), name='comment'),

]
