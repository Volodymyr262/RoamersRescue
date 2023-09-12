from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100, null=True)
    accomodates = models.CharField(max_length=10)
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    reviewer = models.ForeignKey(User, related_name='given_reviews', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[
                                    MinValueValidator(1, message="you can give a host 1-5 stars"),
                                    MaxValueValidator(5, message="you can give a host 1-5 stars")
                                ])