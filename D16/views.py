from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class Board(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'Board.html'
    context_object_name = "board"
    paginate_by = 4


class ShowPost(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'ShowPost.html'
    context_object_name = 'ShowPost'


class CreatePost(PermissionRequiredMixin, CreateView):
    permission_required = ('d16.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'Post_edit.html'
    success_url = reverse_lazy('board')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

