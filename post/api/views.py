from rest_framework import generics
from ..models import Post
from .serializers import PostSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class PostListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Post.published.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Post.published.all()
    serializer_class = PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostSerializer