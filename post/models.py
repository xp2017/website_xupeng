from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='发布')


class Post(models.Model):
    STATUS_CHOICES = (('草稿', '草稿'), ('发布', '发布'))
    title = models.CharField(max_length=250)
    question = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='post_posts')
    image = models.ImageField(upload_to='images/post/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='草稿')
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='post_comments')
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} 回答了该问题'.format(self.author)
