from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

class PostListView(ListView):
    model = Post
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content',
        ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# update view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else: return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
      post = self.get_object()
      if self.request.user == post.author:
          return True
      else: return False

class UserPostListView(ListView):
    model = Post
    template_name = '/blog/user_posts.html'
    context_object_name = 'posts' # sets the context variable name inside the template being called
    paginate_by = 2

    def get_queryset(self): # overrides get
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
