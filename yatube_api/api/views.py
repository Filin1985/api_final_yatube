from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer
from posts.models import Post

class PostViewSet(viewsets.ModelViewSet):
    """
    Endpoint для получения, создания, изменения, удаления постов.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
