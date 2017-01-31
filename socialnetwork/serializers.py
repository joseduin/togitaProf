'''
Created on 23 nov. 2016

@author: ramon
'''
from django.core.urlresolvers import reverse         
from socialnetwork.models import Post, Comment, Resource,User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User    
        fields = ('username','email', 'name', )    
        ordering = ('-created',)    

class OwnerSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User    
        fields = ('username','name')    


class TimelineSerializer(serializers.ModelSerializer):  
    owner =  OwnerSerializer()

    class Meta:
        model = Post    
        fields = ('id','created', 'content', 'url', 'owner', 'comments','resources',)    
        ordering = ('-created',)    
        
#         def owner(self, instance):    
#                 return reverse('user', kwargs={'username':instance.username})    


        

# class PostSerializer(serializers.HyperlinkedModelSerializer):  
#     class Meta:
#         model = Post    
#         fields = ('id','created', 'content', 'url', 'comments', 'resources', 'owner', )    
#         ordering = ('-created',)    

class ResourceSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Resource    
        fields = ('id','created', 'content', 'url', 'post', 'owner')    
        ordering = ('-created',)
        
#         def post(self, instance):    
#                 return reverse('post', kwargs={'id':instance.post.id})        
# 
#         def user(self, instance):    
#                 return reverse('user', kwargs={'username':instance.username})    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment    
        fields = ('id','created', 'content', 'url', 'post', 'owner')    
        ordering = ('-created',)

#         def user(self, instance):    
#                 return reverse('user', kwargs={'username':instance.username})    
#     
#         def post(self, instance):    
#                 return reverse('post', kwargs={'id':instance.post.id})