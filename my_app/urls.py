from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from my_app.views import PostListCreateAPIView, PostDetailApiView, CommentCreateApiView, home
urlpatterns = [
    path(' ',home.as_view(),name='home'),
    path('api/token/',TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token-refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='list-create'),
    path('api/posts/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),
    path('comment/', CommentCreateApiView.as_view(), name='comment'),

]

# fetch('http://127.0.0.1:8000/api/your_resource/', {
#   method: 'GET',
#   headers: {
#     'Authorization': 'Bearer your_new_access_token'
#   }
# })
#   .then(response => response.json())
#   .then(data => console.log(data))
#   .catch(error => console.log('Error:', error));
# Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/posts/" -Method Get -Headers @{Authorization="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4NzQ3MTU2LCJpYXQiOjE3Mzg3NDY4MTksImp0aSI6IjA3ZDVkMjQ0N2VlMzRlMDI4ZjA3NTY5NDE3MDc5YjQ0IiwidXNlcl9pZCI6MX0.8DEcklzXHXrmuFk0GHu_-vB-ler65V240y4oAFPGstI"}
