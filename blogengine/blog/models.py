from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True) #db_index - делает индекс каждому полю
    slug = models.SlugField(max_length=150, unique=True)    #unique - делает каждое поле уникальным
    body = models.TextField(blank=True, db_index=True)      #blank=True - позволяет оставлять поле пустым
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # возвращает ссылку на конкретный пост

    def __str__(self):
        return f'{self.title}'
