from django.urls import path
from .views import HomePageView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', ArticleCreateView.as_view(), name='add_post'),
    path('article/edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/remove/', ArticleDeleteView.as_view(), name='article_remove'),
]
