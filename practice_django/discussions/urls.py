# -*- coding: utf-8 -*-
from django.urls import path, re_path
from discussions.views import DiscussionsDetailView, UserDiscussionsListView
from discussions import views

urlpatterns = [
    path("create/", views.discussion_create, name="create"),
    path(
        "list/user/<str:username>/",
        UserDiscussionsListView.as_view(),
        name="user-discussions-list",
    ),
    # path("post/new/", PostCreateView.as_view(), name="post-create"),
    path(
        "<int:pk>/detail/", DiscussionsDetailView.as_view(), name="discussions-detail"
    ),
]
