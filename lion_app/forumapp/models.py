from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    # postgres 를 사용할 예정이기 때문에 -> postgres 에서는 Text 와 Char 를 같게 취급
    # 그래서 스트링을 다루는 곳에서는 Text 사용 - 공식문서
    name = models.TextField(max_length=100, unique=True)
    is_private = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posts: models.QuerySet["Post"]

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    title = models.TextField(max_length=200)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class TopicGroupUser(models.Model):
    class groupChoices(models.IntegerChoices):
        common = 0
        admin = 1

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    group = models.IntegerField(
        default=0, choices=groupChoices.choices
    )  # 0 = common. 1 = admin
    user = models.ForeignKey(User, on_delete=models.CASCADE)
