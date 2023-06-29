from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post
from django.contrib.auth.models import User

# a = Post.object.filter(author=1).order_by("-date_created")


class UserMixin(object):
    # выборка пользователя
    pass


# class UserPostFormMixin(object):
#     model = Post
#     fields = ["title", "content"]
#     succes_url_redirect = reverse_lazy("user-posts-list")


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    # context_object_name = "blog_post_user_list"

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get("username"))
    #     return Post.objects.filter(author=user).order_by("-date_created")

    def get_context_data(self, **kwargs: Any):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        queryset = Post.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context["blog_post_user_list"] = queryset.order_by("-date_created")
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    # template_name = "blog/post_detail.html"
    context_object_name = "blog_post_detail"
