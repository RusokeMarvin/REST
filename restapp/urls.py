from django.urls import path
from .views import PostsView,Post_details,ShoesView
 
urlpatterns =[
    path('posts/',PostsView),
    path('shoes/',ShoesView),
    path('posts/details/<int:pk>/',Post_details)
]