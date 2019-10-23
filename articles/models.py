from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 유저정보가 없어지면 article 정보도 사라진다
    # settings.py 에서 직접 가지고 온다. models.py 에서만 이걸로 가져오고 다른 곳에선 get_user_model 로 가져온다
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_articles')
    # article.liked_users.all() => 아티클을 좋아하는 유저들
    # users.liked_articles.all() <- related_name => 유저가 좋아하는 아티클들
    
    class Meta:
        ordering = ('-pk', )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-pk']
