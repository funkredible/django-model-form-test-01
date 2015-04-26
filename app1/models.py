from django.db import models


class Article(models.Model):
    text = models.CharField(max_length=255)


class Comment(models.Model):
    article = models.ForeignKey(Article)
    text = models.CharField(max_length=255)
