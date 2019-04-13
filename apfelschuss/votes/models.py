from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from tinymce import HTMLField

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title


class Voting(models.Model):
    title = models.CharField(max_length=160)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    video_url = models.URLField(max_length=200)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    previous_voting = models.ForeignKey(
        'self',
        related_name='previous',
        on_delete=models.SET_NULL,
        blank=True, null=True)
    next_voting = models.ForeignKey(
        'self',
        related_name='next',
        on_delete=models.SET_NULL,
        blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('votes:single', kwargs={
            'id': self.id
        })