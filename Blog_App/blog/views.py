from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog

# Create your views here.

def home(request):
    context = {
        "posts":Blog.objects.all()
    }

    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Blog
    template_name='blog/home.html'
    context_object_name="posts"
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model = Blog

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Blog
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
         "title": 'about'
    }
    return render(request, "blog/about.html", context)