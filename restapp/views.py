from django.shortcuts import render
from .models import Post,Tag
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET','POST'])  
def PostsView(request,tag_name):
    if request.method == 'GET':
        tag = Tag.objects.get(name=tag_name)
        posts= Post.objects.filter(tag=tag) #queryset
        serializer=PostSerializer(posts,many=True) #many is put to True if we have .all(if you have a querySet) in the posts
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) #status means data is created
        else:
            return Response(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])       
def Post_details(request,pk):
    try:
        posts=Post.objects.get(pk=pk)
    except posts.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer=PostSerializer(posts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
    if request.method == 'DELETE':
        posts.delete()
        return Response(status=204)

'''@api_view(['GET'])
def Search(request,title):
    data= Post.objects.get(title= title)
    serializer=PostSerializer(data)
    return Response(serializer.data)'''

@api_view(['GET'])
def Search(request,title):
    data= Post.objects.filter(title__icontains= title)
    serializer=PostSerializer(data,many=True)
    return Response(serializer.data)