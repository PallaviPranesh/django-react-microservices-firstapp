from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializers
import requests

# Create your views here.

class PostAPIView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        #serializer = PostSerializers(posts,many = True)
        return Response(self.formatPost(p) for p in posts)
    
    def formatPost(self,post):
        comments = requests.get('http://127.0.0.1:8001/api/posts/%d/comments' %post.id).json()
        return {
            'id':post.id,
             'title':post.title,
             'description':post.description,
             'comments':[]

            
        }
    
    def post(self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

