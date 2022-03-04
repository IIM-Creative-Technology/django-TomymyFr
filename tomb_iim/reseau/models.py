from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    # a user can like a post only once
    liked_by = models.ManyToManyField('auth.User', related_name='liked_posts', blank=True)