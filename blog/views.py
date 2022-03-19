from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts_list'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'


class ArticleCreateView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'






