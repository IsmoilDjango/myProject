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
#
# $headers = @{
#     "Authorization" = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMTU1NTU3LCJpYXQiOjE3NDE1NTA3NzYsImp0aSI6ImU3NjcxYzgxNzdjZjQ2MDI5NWRjZDRmYzE2NTkyYmY1IiwidXNlcl9pZCI6MX0.ZJZyslq1fbC4GVJmNhVHJyfkb4K0bvfuqrr_ABuQAcw"
# }
#
# Invoke-WebRequest -Uri "https://myproject-5wxp.onrender.com/api/posts/" -Headers $headers -Method Get

# $body = @{
#     "username" = "djangoAdmin5432"
#     "password" = "pin123456"
# } | ConvertTo-Json
#
# Invoke-WebRequest -Uri "https://myproject-5wxp.onrender.com/api/token/" -Method Post -Body $body -ContentType "application/json"
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMTU2MTg1LCJpYXQiOjE3NDE1NTA3NzYsImp0aSI6IjQ0OGYyMzJiNjk0MzRiZDliNmMzZTk0Y2Y2MTQzNjZmIiwidXNlcl9pZCI6MX0.XFIHG5XmGLvpH8DmJ5kXBm1wX1XG_sM9iJN8EsaKnZA
#
# $headers = @{
#     "Authorization" = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMTU5MjQ0LCJpYXQiOjE3NDE1NTQ0NDQsImp0aSI6IjZlNWE3ZmNhZDFlYjRjM2JiNDgzMTVhZDIwODc3YzNkIiwidXNlcl9pZCI6MX0.bYTAXeJe7tAwo4N2Bub8BC1J1XUJeqvMHpOvomp8UzA"
# }
#
# Invoke-WebRequest -Uri "https://myproject-5wxp.onrender.com/api/posts/" -Headers $headers -Method Get
