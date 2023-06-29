# from blinker import receiver_connected
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# from datetime import timezone


# def slugify(s):
#     return django_slugify("".join(alphabet.get(w, w) for w in s.lower()))


class Post(models.Model):
    class Meta:
        verbose_name = "Создать пост"
        verbose_name_plural = "Создать посты"

    title = models.CharField(
        max_length=200, help_text="не более 200 символов", db_index=True
    )
    content = RichTextField(
        max_length=5000, blank=True, null=True, help_text="не более 5000 символов"
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # в url при использовании slug обязательно добавить id + get_absolute_url()
    slug = models.SlugField(max_length=50, unique=True)  # unique=True
    likes_post = models.ManyToManyField(
        User, related_name="post_likes", blank=True, verbose_name="Лайки"
    )
    saves_posts = models.ManyToManyField(
        User,
        related_name="blog_posts_save",
        blank=True,
        verbose_name="Сохранённые посты пользователя",
    )
    # reply = models.ForeignKey(
    #     "self", null=True, related_name="reply_ok", on_delete=models.CASCADE
    # )

    def total_likes(self):
        return self.likes.count()

    def total_saves_posts(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


# @receiver_connected(pre_save, sender=Post)
# def prepopulated_slug(sender, instance, **kwargs):
#     instance.slug - slugify(instance.title)
