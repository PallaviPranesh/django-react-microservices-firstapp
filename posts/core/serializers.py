from rest_framework import serializers
from .models import Post
# Create your views here.

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields ='__all__'

