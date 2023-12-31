from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from pytils.translit import slugify


class Discussion(models.Model):
    class Meta:
        verbose_name = "Дискуссия"
        verbose_name_plural = "Дискуссии"

    title = models.CharField(
        max_length=200, help_text="не более 200 символов", db_index=True
    )
    content = RichTextField(blank=True, null=True, help_text="Не более 5000 символов")
    date_updated = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    likes_discussion = models.ManyToManyField(
        User, related_name="discussion_likes", blank=True, verbose_name="Лайки"
    )
    saves_discussion = models.ManyToManyField(
        User,
        related_name="blog_discussion_save",
        blank=True,
        verbose_name="Сохранённые посты пользователя",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Discussion, self).save(*args, **kwargs)

    def total_likes_discussions(self):
        return self.likes.count()

    def total_saves_discussions(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse("discussion-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
