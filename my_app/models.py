from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts', default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    tags = models.ManyToManyField(Tag, blank=True)

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
        ('archived' ,'Archived'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(r.value for r in ratings) / ratings.count()
        return 0

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='ratings',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField()
    class Meta:
        unique_together = ('post','user')
