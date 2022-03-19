from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts_list'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'


class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'


class ArticleUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'title_tag', 'body']


class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('home')

