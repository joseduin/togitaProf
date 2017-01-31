from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):    
        username = models.TextField(primary_key=True)
        password = models.TextField(models.SET_NULL,blank=True,null=True)
        email = models.TextField(unique=True)
        name = models.TextField()    
        created = models.DateTimeField(auto_now_add=True)

class Post(models.Model):    
        content = models.TextField()    
        created = models.DateTimeField(auto_now_add=True)
        owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Resource(models.Model):
        post = models.ForeignKey(Post, editable=True,
                                    related_name='resources')    
        content = models.TextField()  # Base64 Content
        content_type = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        owner = models.ForeignKey(User,on_delete=models.CASCADE)
                
class Comment(models.Model):    
        post = models.ForeignKey(Post, editable=True,
                                    related_name='comments')    
        content = models.TextField()    
        created = models.DateTimeField(auto_now_add=True) 
        owner = models.ForeignKey(User,on_delete=models.CASCADE)
        
