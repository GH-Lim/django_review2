from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# 중계모델을 만들면 불러올때 불편하다.
# => ManytoManyField
# 중계 모델을 거치지 않고 바로 불러올 수 있다.

class User(AbstractUser):  # 상속
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
