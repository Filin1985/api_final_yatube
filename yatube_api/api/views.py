from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from .permissions import IsAuthOrReadOnly
from .serializers import CommentSerializer, PostSerializer, GroupSerializer, FollowSerializer
from posts.models import Post, Group, User, Follow

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Endpoint для получения группы."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Endpoint для получения, создания, изменения, удаления постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Endpoint для получения, создания, изменения, удаления комментариев.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowViewSet(viewsets.ModelViewSet):
    """
    Endpoint для подписки на автора.
    """
    serializer_class = FollowSerializer
    permission_classes = (IsAuthOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        username = self.request.query_params.get('search')
        if username is not None:
            queryset = queryset.filter(following__username=username)
        return queryset
