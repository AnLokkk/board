from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#
# class Author(models.Model):
#     AuthorUser = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', "Хилы"),
        ('dd', "ДД"),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True,)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=16, choices=TYPE, default='dd')
    upload = models.FileField(upload_to='uploads/')

    def preview(self):
        return self.text[0:64] + '...'


class Reply(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)



