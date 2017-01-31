from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

from rest_framework import viewsets, status
 
from socialnetwork.models import Post, Comment, Resource, User
from socialnetwork.serializers import TimelineSerializer, CommentSerializer,\
    ResourceSerializer, UserSerializer
from rest_framework.response import Response
import json


def index(request):
    data = {}
    return render_to_response('index.html', data, context_instance=RequestContext(request))

def home(request):
    data = {}
    return render_to_response('home.html', data, context_instance=RequestContext(request))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer
    
class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = TimelineSerializer 

    def update(self, request, pk=None):
        pass
    
    def create(self, request):
        json_data = json.loads(request.body)
        
        username = json_data['owner']['username']
         
        user = None
        error_message = ''
 
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            error_message = str(e)
 
        if (user != None):
            new_post = Post()
            new_post.content = json_data['content']
            new_post.owner = user
            new_post.save()
            return Response({'ok' : 'true'})
        else:
            return Response({'ok' : 'false', 'error' : error_message},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all().order_by('-created')
    serializer_class = ResourceSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer