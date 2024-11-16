from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CategoryViewSet, AuthorViewSet, ArticleViewSet, CommentViewSet, ProductViewSet, index)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('', index, name='index'),      
]
