from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)    # дата публикации
    created = models.DateTimeField(auto_now_add=True)       # дата создания
    updated = models.DateTimeField(auto_now=True)           # дата обновления
    status = models.CharField(max_length=2,                 # статус поста
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']     # поле сортировки
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
