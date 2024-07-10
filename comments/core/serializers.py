from rest_framework import serializers
from .models import Comment
# Create your views here.

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'

