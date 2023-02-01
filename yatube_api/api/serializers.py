from posts.models import Comment, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group

    def __str__(self):
        return f'{self.slug}'


class PostSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Group.objects.all())
    author = serializers.StringRelatedField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(
        required=False, many=True, queryset=Comment.objects.all())

    class Meta:
        fields = ('id',
                  'text', 'author', 'image', 'pub_date', 'group', 'comments')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
