from django.shortcuts import render
from .models import Post,Shoe
from .serializers import PostSerializer,ShoeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET','POST'])  
def PostsView(request):
    if request.method == 'GET':
        posts= Post.objects.all() #queryset
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

#SHOE VIEWS

@api_view(['GET','POST'])  
def ShoesView(request):
    if request.method == 'GET':
        shoes= Shoe.objects.all() #queryset
        serializer=ShoeSerializer(shoes,many=True) #many is put to True if we have .all(if you have a querySet) in the posts
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ShoeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) #status means data is created
        else:
            return Response(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])       
def Shoe_details(request,pk):
    try:
        shoes=Shoe.objects.get(pk=pk)
    except shoes.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = PostSerializer(shoes)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer=PostSerializer(shoes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors,status=400)
    if request.method == 'DELETE':
        shoes.delete()
        return Response(status=204)
