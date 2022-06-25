from rest_framework import serializers
from posts.models import Post, Group, Comment, User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('text', 'pub_date', 'author', 'image', 'group')
        
        
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')    


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created')         
    
            
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts', 'comments')
        ref_name = 'ReadOnlyUsers'            