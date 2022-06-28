from rest_framework import viewsets 

from posts.models import Post, Group, Comment, User
from posts.serializers import PostSerializer,  GroupSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsUserOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer     
    

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    