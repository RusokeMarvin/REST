from rest_framework import serializers
from .models import Post,Shoe

'''class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=100)
    email= serializers.EmailField(default='')

    def create(self,validate_data):
        return Post.object.create(validate_data)
    
    def update(self,instance,validate_data):
        instance.title=validate_data.get('title',validate_data.title)
        instance.author=validate_data.get('author',validate_data.author)
        instance.email=validate_data.get('email',validate_data.email)'''

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','email','author']

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ['title','email','author']