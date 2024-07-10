from django.shortcuts import render
from rest_framework.views import APIView
from .models import Comment
from rest_framework.response import Response
from .serializers import CommentSerializers

# Create your views here.


class PostCommentAPIView(APIView):
    def get(self, request, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializers(comments, many=True)
        return Response(serializer.data)
'''
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        '''

class CommentAPIView(APIView):
    def post(self,request):
        serializer = CommentSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

