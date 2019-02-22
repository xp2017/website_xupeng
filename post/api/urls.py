from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'post'

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/<pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('', include(router.urls)),
]