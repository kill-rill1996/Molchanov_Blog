from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Product(models.Model):
    name = models.CharField(max_length=120)


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True) #db_index - делает индекс каждому полю
    slug = models.SlugField(max_length=150, blank=True, unique=True)    #unique - делает каждое поле уникальным
    body = models.TextField(blank=True, db_index=True)      #blank=True - позволяет оставлять поле пустым
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts') #related_name - для связи с классом Tag будет использоваться 'posts'
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # возвращает ссылку на конкретный пост

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']
