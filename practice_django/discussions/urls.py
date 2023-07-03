# -*- coding: utf-8 -*-
from django.urls import path, re_path
from discussions.views import DiscussionDetailView, UserDiscussionListView
from discussions import views

urlpatterns = [
    path(
        "list/user/<str:username>/",
        UserDiscussionListView.as_view(),
        name="user-discussions-list"
    ),
    # path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("create/", views.discussion_create, name="create"),
    path(
        "<int:pk>/detail/", DiscussionDetailView.as_view(), name="discussions-detail"
    ),
]
