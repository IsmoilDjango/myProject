from django.urls import path, include
from rest_framework import routers
# from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from my_app.views import PostListCreateAPIView, PostDetailApiView, CommentCreateApiView
urlpatterns = [
    path('api/token/',TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='list-create'),
    path('api/posts/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
    path('comment/', CommentCreateApiView.as_view(), name='comment'),
]

