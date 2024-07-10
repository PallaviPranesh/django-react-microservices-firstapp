from django.urls import path
from .views import PostAPIView


urlpatterns = [path('posts',PostAPIView.as_view()),
              # path('api/comments/<int:pk>/', PostCommentAPIView.as_view(), name='post-comments'),
               ]