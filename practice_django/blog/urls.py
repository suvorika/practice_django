# -*- coding: utf-8 -*-
from django.urls import path, re_path
from blog.views import UserPostListView, PostCreateView, PostDetailView
from . import views

urlpatterns = [
    path("", views.index, name="index-home"),
    path(
        "posts/user/<str:username>/", UserPostListView.as_view(), name="user-posts-list"
    ),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/detail/", PostDetailView.as_view(), name="post-detail"),
]
