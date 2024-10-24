from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=150)


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    email= models.CharField(max_length=500)
    tag=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    cost=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title
