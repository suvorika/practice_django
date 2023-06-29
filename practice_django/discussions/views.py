from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.dates import timezone_today
from discussions.models import Discussion
from .forms import DiscussionCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post


class UserDiscussionListView(ListView):
    model = Discussion
    template_name = "discussions/user_discussions.html"

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context["discussions_post_user_list"] = queryset.order_by("-date_created")


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = "discussions/discussion_detail.html"
    context_object_name = "discussion_detail"


@login_required
def discussion_create(request):
    if request.method == "POST":
        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()
