from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts_list'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'





