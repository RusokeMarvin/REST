from django.urls import path
from .views import PostsView,Post_details, Search
 
urlpatterns =[
    path('posts/<str:tag_name>/',PostsView),
    path('search/<str:title>/',Search),
    path('posts/details/<int:pk>/',Post_details)
]