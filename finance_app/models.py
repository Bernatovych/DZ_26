from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=50, verbose_name='Category')

    def __str__(self):
        return self.name


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='income')
    money = models.IntegerField(verbose_name='Sum')
    date = models.DateField(auto_now=True)


class Expens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    money = models.IntegerField(verbose_name='Sum')
    date = models.DateField(auto_now=True)

